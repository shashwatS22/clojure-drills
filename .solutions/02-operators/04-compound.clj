(let [total 100]
  (let [total (+ total 20)] (println total)
    (let [total (- total 30)] (println total)
      (let [total (* total 2)] (println total)
        (let [total (/ total 4)] (println total))))))
