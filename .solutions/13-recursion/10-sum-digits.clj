(defn sum-digits [n]
  (if (zero? n) 0 (+ (rem n 10) (sum-digits (quot n 10)))))
