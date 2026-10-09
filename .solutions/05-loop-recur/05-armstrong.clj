(let [n 153]
  (loop [x n sum 0]
    (if (zero? x)
      (println (if (= sum n) "armstrong" "not armstrong"))
      (let [d (rem x 10)]
        (recur (quot x 10) (+ sum (* d d d)))))))
