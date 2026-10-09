(let [n 25]
  (loop [x n bits ()]
    (if (zero? x)
      (println (apply str (reverse bits)))
      (recur (quot x 2) (conj bits (rem x 2))))))
