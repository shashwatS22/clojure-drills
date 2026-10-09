(ns runner.watch
  (:require [babashka.fs :as fs]
            [clojure.string :as str]
            [runner.progress :as progress]
            [runner.report :as report]
            [runner.resolve :as resolve]
            [runner.run-one :as run-one]))

(defn- debounce-ms [] 120)

(defn- watchable-rel? [rel-path]
  (and (str/starts-with? rel-path "levels/")
       (str/ends-with? rel-path ".clj")
       (not (str/includes? rel-path "/helpers/"))
       (not (str/ends-with? rel-path "_test.clj"))))

(defn- rel-path [root abs-path]
  (let [root (str (fs/normalize (str root)))
        abs (str (fs/normalize abs-path))]
    (when (str/starts-with? abs root)
      (subs abs (inc (count root))))))

(defn strict-allowed?
  [id config root]
  (if-not (:strict-progression config true)
    true
    (let [{:keys [level]} (resolve/parse-id id)
          prev (resolve/previous-level level)]
      (if (nil? prev)
        true
        (let [passed (progress/passed-ids :root root)]
          (if (resolve/level-complete? prev passed :root root)
            true
            (do
              (report/print-progression-block
               (resolve/first-unfinished-in-level prev passed :root root))
              false)))))))

(defn handle-change!
  [root rel config]
  (when (watchable-rel? rel)
    (let [abs (str (fs/path root rel))
          id (resolve/id-from-abs-path abs :root root)]
      (when id
        (when (strict-allowed? id config root)
          (let [result (run-one/run-exercise abs :id id)
                _ (progress/record-attempt! result :root root)]
            (report/print-result result :config config :root root)))))))

(defn- all-exercise-files [root]
  (->> (fs/glob root "levels/**/*.clj")
       (map str)
       (filter #(not (str/includes? % "/helpers/")))
       (filter #(not (str/ends-with? % "_test.clj")))))

(defn- file-mtime [f]
  (.toMillis (java.nio.file.Files/getLastModifiedTime
              (java.nio.file.Paths/get f (into-array String []))
              (into-array java.nio.file.LinkOption []))))

(defn start! []
  (let [root (resolve/repo-root)
        config (progress/load-config root)
        mtimes (atom {})
        pending (atom {})]
    (report/print-banner)
    (println (report/dim "Watching levels/ — save any exercise to check it.\n"))
    (doseq [f (all-exercise-files root)]
      (swap! mtimes assoc f (file-mtime f)))
    (loop []
      (doseq [f (all-exercise-files root)
              :let [t (file-mtime f)
                    prev (get @mtimes f)]
              :when (and prev (not= prev t))]
        (swap! mtimes assoc f t)
        (when-let [rel (rel-path root f)]
          (swap! pending assoc rel (System/currentTimeMillis))))
      (doseq [[rel ts] (vec @pending)]
        (when (>= (- (System/currentTimeMillis) ts) (debounce-ms))
          (when (= ts (get @pending rel))
            (swap! pending dissoc rel)
            (handle-change! root rel config))))
      (Thread/sleep 150)
      (recur))))
