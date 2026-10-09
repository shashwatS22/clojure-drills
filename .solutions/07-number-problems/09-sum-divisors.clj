(let [n 28]
  (println (reduce + (filter #(zero? (rem n %)) (range 1 (inc n))))))
