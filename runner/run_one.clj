(ns runner.run-one
  (:require [babashka.fs :as fs]
            [babashka.process :as process]
            [clojure.edn :as edn]
            [runner.grade :as grade]
            [runner.resolve :as resolve]))

(defn- exercise-cwd [abs-path level-name root]
  (if (and level-name (re-matches #"1[6-9]-.*" level-name))
    (str root)
    (str (fs/parent abs-path))))

(def ^:private clojure-cli-levels
  #{"17-compojure" "19-jetty"})

(defn- config []
  (try
    (edn/read-string (slurp (str (fs/path (resolve/repo-root) "config.edn"))))
    (catch Exception _ {:timeout-ms 5000})))

(defn timeout-for-level [level-name cfg]
  (or (get-in cfg [:level-timeout-ms level-name])
      (:timeout-ms cfg 5000)))

(defn- exercise-command [abs-path level-name root]
  (if (contains? clojure-cli-levels level-name)
    ["clojure" "-M:run-exercise" abs-path]
    ["bb" abs-path]))

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

(defn run-test-exercise [abs-path test-path timeout-ms level-name root]
  (let [cwd (exercise-cwd abs-path level-name root)
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

(defn run-output-exercise [abs-path expected timeout-ms level-name root]
  (let [cwd (exercise-cwd abs-path level-name root)
        {:keys [stdout stderr exit duration-ms timeout?]}
        (run-process (exercise-command abs-path level-name root) cwd timeout-ms)]
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
        cfg (config)
        timeout-ms (or timeout-ms (timeout-for-level level cfg))
        mode (resolve/grading-mode id :root root)
        hint (resolve/hint-for id)
        body (case mode
               :output
               (if-let [exp-path (when (fs/exists? (resolve/expected-path id :root root))
                                  (resolve/expected-path id :root root))]
                 (run-output-exercise abs-path (slurp exp-path) timeout-ms level root)
                 {:status :missing-expected})

               :test
               (run-test-exercise abs-path (resolve/test-path id :root root) timeout-ms level root)

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
  [abs-path timeout-ms & {:keys [level-name root]}]
  (let [root (or root (resolve/repo-root))
        level-name (or level-name
                       (:level (resolve/parse-id (resolve/id-from-abs-path abs-path :root root))))
        cwd (exercise-cwd abs-path level-name root)
        {:keys [stdout stderr exit duration-ms timeout?]}
        (run-process (exercise-command abs-path level-name root) cwd timeout-ms)]
    (cond
      timeout? {:status :timeout :duration-ms duration-ms}
      (not (zero? exit)) {:status :error :stderr stderr :duration-ms duration-ms}
      :else {:status :pass :actual stdout :duration-ms duration-ms})))

(defn slurp-config [] (config))
