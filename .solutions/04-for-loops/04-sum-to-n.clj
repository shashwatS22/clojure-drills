(let [n 100]
  (loop [i 1 sum 0]
    (if (> i n) (println sum)
      (recur (inc i) (+ sum i)))))
