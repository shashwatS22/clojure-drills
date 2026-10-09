(let [a [1 2 3 4 6] b [2 3 5]]
  (println (clojure.string/join " " (sort (set (concat a b))))))
