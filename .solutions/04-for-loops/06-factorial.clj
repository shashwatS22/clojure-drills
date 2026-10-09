(let [n 6]
  (loop [i 2 acc 1]
    (if (> i n) (println acc)
      (recur (inc i) (* acc i)))))
