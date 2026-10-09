(let [a 120 b 45]
  (loop [x a y b] (if (zero? y) (println x) (recur y (rem x y)))))
