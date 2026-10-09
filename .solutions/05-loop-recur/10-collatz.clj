(let [n 27]
  (loop [x n steps 0]
    (if (= x 1) (println steps)
      (recur (if (even? x) (/ x 2) (+ (* 3 x) 1)) (inc steps)))))
