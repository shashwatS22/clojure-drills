(let [n 1000000]
  (loop [x n c 0]
    (if (zero? x) (println c)
      (recur (quot x 10) (inc c)))))
