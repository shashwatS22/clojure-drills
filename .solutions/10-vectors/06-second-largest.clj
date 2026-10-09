(let [arr [12 35 1 10 34 35] sorted (sort > (distinct arr))]
  (println (second sorted)))
