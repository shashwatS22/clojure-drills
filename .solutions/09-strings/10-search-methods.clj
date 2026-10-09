(require '[clojure.string :as str])
(let [s "javascript"]
  (println (str/includes? s "script"))
  (println (str/starts-with? s "java"))
  (println (str/ends-with? s "x"))
  (println (str/index-of s "a")))
