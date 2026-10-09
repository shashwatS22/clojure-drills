(let [arr [1 2 2 5 9]]
  (println (every? true? (map >= (rest arr) arr))))
