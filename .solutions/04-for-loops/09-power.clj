(let [base 3 exp 5]
  (loop [e exp acc 1]
    (if (zero? e) (println acc)
      (recur (dec e) (* acc base)))))
