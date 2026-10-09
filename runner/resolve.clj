(ns runner.resolve
  (:require [babashka.fs :as fs]
            [clojure.string :as str]
            [runner.hints :as hints]))

(defn repo-root []
  (fs/cwd))

(defn levels-dir [root]
  (fs/path root "levels"))

(defn list-levels
  ([] (list-levels (repo-root)))
  ([root]
   (->> (fs/glob root "levels/*")
        (map str)
        (filter fs/directory?)
        (sort)
        (map fs/file-name))))

(defn level-number [level-name]
  (some-> level-name (str/split #"-" 2) first Integer/parseInt))

(defn list-exercises-in-level
  [level-name & {:keys [root include-tests?]}]
  (let [root (or root (repo-root))
        dir (fs/path root "levels" level-name)]
    (->> (fs/glob root (str "levels/" level-name "/*.clj"))
         (map str)
         (map fs/file-name)
         (filter #(not (str/ends-with? % "_test.clj")))
         (sort))))

(defn exercise-id
  "level-folder/basename-without-.clj"
  [level-name exercise-file]
  (str level-name "/" (str/replace exercise-file #"\.clj$" "")))

(defn parse-id
  [id]
  (let [parts (str/split id #"/" 2)]
    (when (= 2 (count parts))
      {:level (first parts) :basename (second parts)})))

(defn exercise-path
  [id & {:keys [root solutions?]}]
  (let [{:keys [level basename]} (parse-id id)
        root (or root (repo-root))
        base (if solutions? ".solutions" "levels")
        file (str basename ".clj")]
    (str (fs/path root base level file))))

(defn expected-path [id & {:keys [root]}]
  (let [{:keys [level basename]} (parse-id id)
        root (or root (repo-root))]
    (str (fs/path root "levels" level (str basename ".expected.txt")))))

(defn test-path [id & {:keys [root]}]
  (let [{:keys [level basename]} (parse-id id)
        root (or root (repo-root))]
    (str (fs/path root "levels" level (str basename "_test.clj")))))

(defn stub-path [id & {:keys [root]}]
  (let [{:keys [level basename]} (parse-id id)
        root (or root (repo-root))]
    (str (fs/path root "stubs" level (str basename ".clj")))))

(defn solution-path [id & {:keys [root]}]
  (exercise-path id :root root :solutions? true))

(defn all-exercise-ids
  ([] (all-exercise-ids (repo-root)))
  ([root]
   (for [level (list-levels root)
         ex (list-exercises-in-level level :root root)]
     (exercise-id level ex))))

(defn id-from-abs-path
  [abs-path & {:keys [root]}]
  (let [root (str (fs/normalize (str (or root (repo-root)))))
        abs (str (fs/normalize abs-path))
        prefix (str root "/levels/")]
    (when (str/starts-with? abs prefix)
      (let [rest (subs abs (count prefix))
            idx (.lastIndexOf rest "/")
            level (subs rest 0 idx)
            file (subs rest (inc idx))]
        (when (str/ends-with? file ".clj")
          (exercise-id level (str/replace file #"\.clj$" "")))))))

(defn grading-mode
  [id & {:keys [root]}]
  (let [exp (expected-path id :root root)
        tst (test-path id :root root)]
    (cond
      (fs/exists? tst) :test
      (fs/exists? exp) :output
      :else :missing-expected)))

(defn first-unfinished-in-level
  [level-name passed-ids & {:keys [root]}]
  (some (fn [ex]
          (let [id (exercise-id level-name ex)]
            (when-not (contains? passed-ids id) id)))
        (list-exercises-in-level level-name :root root)))

(defn level-complete?
  [level-name passed-ids & {:keys [root]}]
  (every? #(contains? passed-ids (exercise-id level-name %))
          (list-exercises-in-level level-name :root root)))

(defn previous-level [level-name]
  (let [n (level-number level-name)]
    (when (and n (> n 1))
      (some #(when (= (level-number %) (dec n)) %)
            (list-levels)))))

(defn hint-for [id]
  (get (hints/all) id))
