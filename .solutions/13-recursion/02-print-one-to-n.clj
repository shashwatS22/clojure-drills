(defn print-1-to [n]
  (when (<= 1 n)
    (print-1-to (dec n))
    (println n)))
(print-1-to 5)
