(defn fib [n]
  (cond (= n 0) 0 (= n 1) 1 :else (+ (fib (dec n)) (fib (- n 2)))))
