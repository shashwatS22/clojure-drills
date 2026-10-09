(ns runner.run-exercise-cli
  "Load and run a single exercise .clj file (Clojure CLI — Compojure/Jetty)."
  (:require [clojure.java.io :as io]))

(defn -main [& [path & _]]
  (when-not path
    (binding [*out* *err*]
      (println "Usage: clojure -M:run-exercise <absolute-path-to-exercise.clj>"))
    (System/exit 1))
  (let [f (io/file path)]
    (when-not (.exists f)
      (binding [*out* *err*]
        (println "File not found:" path))
      (System/exit 1))
    (load-file path)))
