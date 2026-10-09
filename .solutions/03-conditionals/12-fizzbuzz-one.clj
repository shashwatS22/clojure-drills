(let [n 15]
  (println (cond
             (zero? (rem n 15)) "FizzBuzz"
             (zero? (rem n 3)) "Fizz"
             (zero? (rem n 5)) "Buzz"
             :else (str n))))
