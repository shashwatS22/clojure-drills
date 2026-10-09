(defn prime? [x]
  (and (> x 1)
       (not (some #(zero? (rem x %))
                  (range 2 (inc (int (Math/sqrt x))))))))

(let [k 20]
  (println (nth (filter prime? (range 2 1000)) (dec k))))
