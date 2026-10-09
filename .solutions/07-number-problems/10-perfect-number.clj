(let [n 496 sum-proper (reduce + (filter #(and (zero? (rem n %)) (not= % n)) (range 1 n)))]
  (println (if (= sum-proper n) "perfect" "not perfect")))
