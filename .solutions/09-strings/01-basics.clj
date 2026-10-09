(require '[clojure.string :as str])
(let [s "JavaScript"]
  (println (count s))
  (println (str/upper-case s))
  (println (str/lower-case s)))
