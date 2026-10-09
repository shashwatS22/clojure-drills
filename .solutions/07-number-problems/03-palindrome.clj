(let [n 1221 orig n]
  (loop [x n rev 0]
    (if (zero? x) (println (= orig rev)) (recur (quot x 10) (+ (* rev 10) (rem x 10))))))
