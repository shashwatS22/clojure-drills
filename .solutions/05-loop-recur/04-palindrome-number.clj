(let [n 12321 orig n rev 0]
  (loop [x n rev 0]
    (if (zero? x)
      (println (if (= orig rev) "palindrome" "not palindrome"))
      (recur (quot x 10) (+ (* rev 10) (rem x 10))))))
