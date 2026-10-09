(let [n 9375]
  (loop [x n sum 0]
    (if (zero? x) (println sum)
      (recur (quot x 10) (+ sum (rem x 10))))))
