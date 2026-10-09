(let [a 12 b 18 gcd (loop [x a y b] (if (zero? y) x (recur y (rem x y))))]
  (println (/ (* a b) gcd)))
