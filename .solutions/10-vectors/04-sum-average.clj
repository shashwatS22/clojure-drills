(let [arr [4 8 15 16 23 42]
      sum (reduce + arr)]
  (println sum)
  (println (format "%.2f" (/ (double sum) (count arr)))))
