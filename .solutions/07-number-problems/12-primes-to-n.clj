(let [n 30 prime? (fn [x] (and (> x 1) (not (some #(zero? (rem x %)) (range 2 (inc (int (Math/sqrt x))))))))]
  (println (clojure.string/join " " (filter prime? (range 2 (inc n))))))
