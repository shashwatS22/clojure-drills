(doseq [i (range 1 21)] (println (cond (zero? (rem i 15)) "FizzBuzz" (zero? (rem i 3)) "Fizz" (zero? (rem i 5)) "Buzz" :else i)))
