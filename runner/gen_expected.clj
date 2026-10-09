(ns runner.gen-expected
  (:require [babashka.fs :as fs]
            [clojure.string :as str]
            [runner.resolve :as resolve]
            [runner.run-one :as run-one]))

(defn generate-one! [id]
  (let [root (resolve/repo-root)
        sol (resolve/solution-path id :root root)
        exp (resolve/expected-path id :root root)
        tst (resolve/test-path id :root root)
        cfg (run-one/slurp-config)
        level (:level (resolve/parse-id id))
        timeout-ms (run-one/timeout-for-level level cfg)]
    (when-not (fs/exists? tst)
      (let [result (run-one/capture-stdout sol timeout-ms :level-name level)]
        (case (:status result)
          :pass
          (do
            (when (str/blank? (:actual result))
              (throw (ex-info "Empty output — not writing expected file" {:id id})))
            (spit exp (:actual result))
            (println "Wrote" exp))

          :error (throw (ex-info "Solution errored" {:id id :stderr (:stderr result)}))
          :timeout (throw (ex-info "Solution timed out" {:id id}))
          (throw (ex-info "Cannot generate expected" {:id id :status (:status result)})))))))

(defn generate-all! []
  (doseq [id (resolve/all-exercise-ids)]
    (generate-one! id)))

(defn -main [& _]
  (generate-all!))
