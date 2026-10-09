(let [n 5]
  (loop [i 1]
    (when (<= i n)
      (println i)
      (recur (inc i)))))
