(let [arr [1 [2 3] [4 [5]]]]
  (println (clojure.string/join " " (flatten arr)))
  (println (clojure.string/join " " (clojure.core/flatten arr))))
