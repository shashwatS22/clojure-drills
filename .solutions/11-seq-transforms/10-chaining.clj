(->> (range 1 11) (filter even?) (map #(* % %)) (reduce +) println)
