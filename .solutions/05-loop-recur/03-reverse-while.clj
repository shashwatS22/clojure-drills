(let [n 9081]
  (loop [x n rev 0]
    (if (zero? x) (println rev)
      (recur (quot x 10) (+ (* rev 10) (rem x 10))))))
