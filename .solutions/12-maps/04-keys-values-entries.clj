(let [scores {:math 90 :science 85 :art 72}]
  (println (clojure.string/join " " (map name (keys scores))))
  (println (clojure.string/join " " (vals scores)))
  (println (count scores)))
