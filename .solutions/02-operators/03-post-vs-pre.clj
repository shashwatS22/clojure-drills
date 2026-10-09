(let [x 5]
  (println x)
  (let [x (inc x)]
    (println x)
    (let [x (inc x)]
      (println x)
      (println x))))
