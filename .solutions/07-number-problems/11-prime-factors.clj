(let [n 360]
  (loop [x n d 2 factors []]
    (cond
      (= x 1) (println (clojure.string/join " " factors))
      (zero? (rem x d)) (recur (quot x d) d (conj factors d))
      :else (recur x (inc d) factors))))
