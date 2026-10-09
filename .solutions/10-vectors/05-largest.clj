(let [arr [3 41 7 41 19]]
  (println (reduce (fn [acc x] (if (> x acc) x acc)) arr)))
