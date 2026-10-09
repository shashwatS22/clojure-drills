(let [arr [0 1 2 4 5] n 5 expected (* n (+ n 1) (/ 1 2))]
  (println (- expected (reduce + arr))))
