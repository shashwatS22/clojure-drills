(defn is-palindrome [s]
  (let [n (count s)]
    (loop [i 0 j (dec n)]
      (if (>= i j) true
        (if (= (nth s i) (nth s j)) (recur (inc i) (dec j)) false)))))
