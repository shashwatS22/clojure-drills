(ns runner.cli
  (:require [babashka.fs :as fs]
            [clojure.string :as str]
            [runner.gen-expected :as gen]
            [runner.progress :as progress]
            [runner.report :as report]
            [runner.resolve :as resolve]
            [runner.run-one :as run-one]
            [runner.verify-readmes :as verify]))

(defn- usage []
  (println "Usage:")
  (println "  bb dev")
  (println "  bb check <exercise-id>")
  (println "  bb check:level <NN> [--solutions]")
  (println "  bb progress")
  (println "  bb solution <exercise-id> [--force]")
  (println "  bb reset <exercise-id|level> [--yes]")
  (println "  bb gen:expected"))

(defn cmd-check [id]
  (when-not id
    (usage)
    (System/exit 1))
  (let [root (resolve/repo-root)
        config (progress/load-config root)
        result (run-one/run-exercise-by-id id)]
    (progress/record-attempt! result :root root)
    (report/print-result result :config config :root root)
    (when (not= :pass (:status result))
      (System/exit 1))))

(defn cmd-check-level [arg & rest-args]
  (let [solutions? (some #(= % "--solutions") rest-args)
        nn (str/replace (or arg "") #"^0+" "")
        level (some #(when (= (str (resolve/level-number %)) nn) %)
                    (resolve/list-levels))
        _ (when-not level
            (println "Unknown level:" arg)
            (System/exit 1))
        root (resolve/repo-root)
        results (for [ex (resolve/list-exercises-in-level level :root root)
                      :let [id (resolve/exercise-id level ex)]]
                  (run-one/run-exercise-by-id id :solutions? solutions?))]
    (doseq [r results]
      (when-not solutions?
        (progress/record-attempt! r :root root)))
    (report/print-level-summary results)
    (when (some #(not= :pass (:status %)) results)
      (System/exit 1))))

(defn cmd-progress [_]
  (report/print-dashboard (progress/dashboard-data)))

(defn cmd-solution [id & rest-args]
  (let [force? (some #(= % "--force") rest-args)
        root (resolve/repo-root)
        config (progress/load-config root)
        unlock (:solution-unlock-after-failures config 3)
        prog (progress/read-progress :root root)
        entry (get-in prog [:exercises id])
        failures (or (:attempts entry) 0)
        passed? (= "pass" (:status entry))
        path (resolve/solution-path id :root root)]
    (when-not (fs/exists? path)
      (println "No solution for" id)
      (System/exit 1))
    (when (and (not force?) (not passed?) (< failures unlock))
      (println (str "Solution locked. Fail this exercise "
                    (- unlock failures)
                    " more time(s), or use --force."))
      (System/exit 1))
    (progress/mark-solution-viewed! id :root root)
    (println (slurp path))))

(defn restore-stub! [id root]
  (let [stub (resolve/stub-path id :root root)
        dest (resolve/exercise-path id :root root)]
    (when-not (fs/exists? stub)
      (println "No stub for" id)
      (System/exit 1))
    (fs/copy stub dest {:replace-existing true})))

(defn cmd-reset [target & rest-args]
  (let [yes? (some #(= % "--yes") rest-args)
        root (resolve/repo-root)]
    (when-not target
      (usage)
      (System/exit 1))
    (when-not yes?
      (println (str "This will restore stub(s) and clear progress for " target ". Pass --yes to confirm."))
      (System/exit 1))
    (if-let [parsed (resolve/parse-id target)]
      (do
        (restore-stub! target root)
        (progress/clear-exercise! target :root root)
        (println "Reset" target))
      (let [level (some #(when (str/starts-with? % (str target "-")) %) (resolve/list-levels))]
        (when-not level
          (println "Unknown target:" target)
          (System/exit 1))
        (doseq [ex (resolve/list-exercises-in-level level :root root)
                :let [id (resolve/exercise-id level ex)]]
          (restore-stub! id root))
        (progress/clear-level! level :root root)
        (println "Reset level" level)))))

(defn -main [& args]
  (case (first args)
    "dev" ((requiring-resolve 'runner.watch/start!))
    "check" (cmd-check (second args))
    "check:level" (apply cmd-check-level (rest args))
    "progress" (cmd-progress nil)
    "solution" (apply cmd-solution (rest args))
    "reset" (apply cmd-reset (rest args))
    "gen:expected" (gen/generate-all!)
    "verify:readmes" (verify/verify-all!)
    (do (usage) (System/exit 1))))
