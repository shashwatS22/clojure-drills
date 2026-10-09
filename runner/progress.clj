(ns runner.progress
  (:require [babashka.fs :as fs]
            [clojure.edn :as edn]
            [clojure.string :as str]
            [runner.resolve :as resolve]))

(defn progress-file [root]
  (str (fs/path (or root (resolve/repo-root)) "progress.edn")))

(defn load-config [root]
  (let [p (str (fs/path (or root (resolve/repo-root)) "config.edn"))]
    (when (fs/exists? p)
      (edn/read-string (slurp p)))))

(defn read-progress
  [& {:keys [root]}]
  (let [root (or root (resolve/repo-root))
        pf (progress-file root)]
    (if (fs/exists? pf)
      (try
        (edn/read-string (slurp pf))
        (catch Exception e
          (let [bak (str pf ".bak")]
            (fs/copy pf bak {:replace-existing true})
            (println "Warning: progress.edn was corrupt; backed up to progress.edn.bak")
            {:version 1 :started-at (str (java.time.Instant/now)) :exercises {}})))
      {:version 1
       :started-at (str (java.time.Instant/now))
       :exercises {}})))

(defn write-progress!
  [data & {:keys [root]}]
  (let [root (or root (resolve/repo-root))
        pf (progress-file root)
        tmp (str pf ".tmp")]
    (spit tmp (pr-str data))
    (fs/move tmp pf {:replace-existing true})))

(defn passed-ids
  [& {:keys [root]}]
  (let [prog (read-progress :root root)]
    (set (for [[id m] (:exercises prog)
               :when (= "pass" (:status m))]
           id))))

(defn record-attempt!
  [result & {:keys [root solutions?]}]
  (when-not solutions?
    (let [root (or root (resolve/repo-root))
          prog (read-progress :root root)
          id (:id result)
          prev (get-in prog [:exercises id])
          attempts (inc (or (:attempts prev) 0))
          now (str (java.time.Instant/now))
          status (name (:status result))
          entry (merge (or prev {})
                       {:status status
                        :attempts attempts
                        :last-run-at now}
                       (when (and (= status "pass") (not (:first-pass-at prev)))
                         {:first-pass-at now}))]
      (write-progress! (assoc-in prog [:exercises id] entry) :root root))))

(defn mark-solution-viewed!
  [id & {:keys [root]}]
  (let [root (or root (resolve/repo-root))
        prog (read-progress :root root)
        prev (get-in prog [:exercises id] {})]
    (write-progress! (assoc-in prog [:exercises id]
                               (assoc prev :solution-viewed true))
                     :root root)))

(defn clear-exercise!
  [id & {:keys [root]}]
  (let [root (or root (resolve/repo-root))
        prog (read-progress :root root)]
    (write-progress! (update prog :exercises dissoc id) :root root)))

(defn clear-level!
  [level & {:keys [root]}]
  (let [root (or root (resolve/repo-root))
        prog (read-progress :root root)
        ids (set (map #(resolve/exercise-id level %)
                      (resolve/list-exercises-in-level level :root root)))]
    (write-progress!
     (update prog :exercises #(into {} (remove (fn [[k _]] (contains? ids k)) %)))
     :root root)))

(defn dashboard-data
  [& {:keys [root]}]
  (let [root (or root (resolve/repo-root))
        prog (read-progress :root root)
        passed (passed-ids :root root)
        levels (resolve/list-levels root)]
    {:levels
     (for [level levels
           :let [exs (resolve/list-exercises-in-level level :root root)
                 done (count (filter #(contains? passed (resolve/exercise-id level %)) exs))
                 total (count exs)]]
       {:name level :done done :total total})
     :total-done (count passed)
     :total-exercises (count (resolve/all-exercise-ids root))
     :exercises (:exercises prog)}))
