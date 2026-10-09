(ns runner.run-one
  (:require [babashka.fs :as fs]
            [babashka.process :as process]
            [clojure.edn :as edn]
            [runner.grade :as grade]
            [runner.resolve :as resolve]))

(defn- exercise-cwd [abs-path]
  (str (fs/parent abs-path)))

(defn- config []
  (try
    (edn/read-string (slurp (str (fs/path (resolve/repo-root) "config.edn"))))
    (catch Exception _ {:timeout-ms 5000})))

(defn- run-process [command cwd timeout-ms]
  (let [start (System/currentTimeMillis)]
    (try
      (let [proc (process/shell {:cmd command
                                 :out :string
                                 :err :string
                                 :dir cwd
                                 :timeout timeout-ms})]
        {:stdout (or (:out proc) "")
         :stderr (or (:err proc) "")
         :exit (or (:exit proc) 0)
         :duration-ms (- (System/currentTimeMillis) start)
         :timeout? false})
      (catch Exception e
        (let [msg (or (ex-message e) (.getMessage e) "")]
          (if (re-find #"(?i)timeout" msg)
            {:timeout? true
             :duration-ms (- (System/currentTimeMillis) start)}
            {:timeout? false
             :stderr msg
             :stdout ""
             :exit 1
             :duration-ms (- (System/currentTimeMillis) start)}))))))

(defn run-test-exercise [abs-path test-path timeout-ms]
  (let [cwd (exercise-cwd abs-path)
        runner (str (fs/path (resolve/repo-root) "runner" "run_tests.clj"))
        {:keys [stdout stderr exit duration-ms timeout?]}
        (run-process ["bb" runner abs-path test-path] cwd timeout-ms)]
    (cond
      timeout? {:status :timeout :duration-ms duration-ms}
      (zero? exit) {:status :pass :duration-ms duration-ms}
      :else {:status :fail
             :duration-ms duration-ms
             :stderr (str stderr stdout)
             :actual stdout})))

(defn run-output-exercise [abs-path expected timeout-ms]
  (let [cwd (exercise-cwd abs-path)
        {:keys [stdout stderr exit duration-ms timeout?]}
        (run-process ["bb" abs-path] cwd timeout-ms)]
    (cond
      timeout? {:status :timeout :duration-ms duration-ms}
      (not (zero? exit))
      {:status :error :stderr stderr :stdout stdout :duration-ms duration-ms}

      :else
      (let [cmp (grade/compare-outputs expected stdout)]
        (if (:match? cmp)
          {:status :pass :actual stdout :duration-ms duration-ms}
          {:status :fail
           :actual stdout
           :expected expected
           :comparison cmp
           :duration-ms duration-ms})))))

(defn enrich-result [result]
  (if (= :fail (:status result))
    (assoc result :diff (grade/build-diff (:comparison result) 20))
    result))

(defn run-exercise
  [abs-path & {:keys [id timeout-ms]}]
  (let [root (resolve/repo-root)
        id (or id (resolve/id-from-abs-path abs-path :root root))
        parsed (resolve/parse-id id)
        level (:level parsed)
        timeout-ms (or timeout-ms (:timeout-ms (config)) 5000)
        mode (resolve/grading-mode id :root root)
        hint (resolve/hint-for id)
        body (case mode
               :output
               (if-let [exp-path (when (fs/exists? (resolve/expected-path id :root root))
                                  (resolve/expected-path id :root root))]
                 (run-output-exercise abs-path (slurp exp-path) timeout-ms)
                 {:status :missing-expected})

               :test
               (run-test-exercise abs-path (resolve/test-path id :root root) timeout-ms)

               {:status :missing-expected})]
    (merge {:id id :level level :mode (name mode) :hint hint} body)))

(defn run-exercise-by-id
  [id & {:keys [solutions?] :as opts}]
  (let [path (if solutions?
               (resolve/solution-path id)
               (resolve/exercise-path id))]
    (-> (apply run-exercise path (concat [:id id] (seq (dissoc opts :solutions?))))
        enrich-result)))

(defn capture-stdout
  "Run a script and return stdout (for gen:expected)."
  [abs-path timeout-ms]
  (let [cwd (exercise-cwd abs-path)
        {:keys [stdout stderr exit duration-ms timeout?]}
        (run-process ["bb" abs-path] cwd timeout-ms)]
    (cond
      timeout? {:status :timeout :duration-ms duration-ms}
      (not (zero? exit)) {:status :error :stderr stderr :duration-ms duration-ms}
      :else {:status :pass :actual stdout :duration-ms duration-ms})))

(defn slurp-config [] (config))
