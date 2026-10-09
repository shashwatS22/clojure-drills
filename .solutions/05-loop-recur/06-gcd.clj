(let [a 48 b 18]
  (loop [x a y b]
    (if (zero? y) (println x)
      (recur y (rem x y)))))
