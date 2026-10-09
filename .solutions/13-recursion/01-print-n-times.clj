(defn print-times [n]
  (when (pos? n)
    (println "learning")
    (print-times (dec n))))
(print-times 4)
