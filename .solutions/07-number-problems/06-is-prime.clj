(let [n 97
      prime? (and (> n 1)
                  (not (some #(zero? (rem n %))
                             (range 2 (inc (int (Math/sqrt n)))))))]
  (println (if prime? "prime" "not prime")))
