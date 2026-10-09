(let [n 10]
  (loop [count 0 a 0 b 1]
    (when (< count n)
      (println a)
      (recur (inc count) b (+ a b)))))
