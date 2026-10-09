(let [year 2100]
  (println (if (and (zero? (rem year 4))
                      (or (not (zero? (rem year 100))) (zero? (rem year 400))))
                 "leap" "not leap")))
