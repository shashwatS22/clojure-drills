(defn print-down [n]
  (when (pos? n)
    (println n)
    (print-down (dec n))))
(print-down 5)
