(defn sum-to [n]
  (if (<= n 1) n (+ n (sum-to (dec n)))))
