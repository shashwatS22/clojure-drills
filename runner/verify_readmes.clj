(ns runner.verify-readmes
  (:require [babashka.fs :as fs]
            [babashka.process :as process]
            [clojure.string :as str]
            [runner.resolve :as resolve]))

(defn extract-clojure-blocks [markdown]
  (let [parts (str/split markdown #"```(?:clojure|clj)\s*\n")]
    (butlast
     (map first
          (map #(str/split % #"```" 2) (rest parts))))))

(defn verify-file! [readme-path]
  (let [content (slurp readme-path)
        blocks (extract-clojure-blocks content)]
    (doseq [[i block] (map vector (range) blocks)]
      (let [tmp (str (fs/path (fs/temp-dir) (str "readme-snippet-" i ".clj")))]
        (spit tmp block)
        (let [proc (process/shell {:cmd ["bb" tmp]
                                    :out :string
                                    :err :string})]
          (when (not (zero? (:exit proc)))
            (println "FAIL snippet" (inc i) "in" readme-path)
            (println (:err proc))
            (System/exit 1)))))))

(defn verify-all! []
  (doseq [level (resolve/list-levels)
          :let [p (str (fs/path (resolve/repo-root) "levels" level "README.md"))]
          :when (fs/exists? p)]
    (verify-file! p))
  (println "All README snippets OK."))

(defn -main [& _]
  (verify-all!))
