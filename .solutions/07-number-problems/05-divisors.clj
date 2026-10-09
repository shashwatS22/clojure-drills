(let [n 36]
  (println (clojure.string/join " " (filter #(zero? (rem n %)) (range 1 (inc n))))))
