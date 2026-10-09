(let [n 371 digits (loop [x n ds []] (if (zero? x) ds (recur (quot x 10) (conj ds (rem x 10)))))]
  (println (= n (reduce + (map #(* % % %) digits)))))
