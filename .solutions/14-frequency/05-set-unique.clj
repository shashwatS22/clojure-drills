(let [arr [1 2 2 3 3 3] u (sort (set arr))]
  (println (clojure.string/join " " u))
  (println (count u)))
