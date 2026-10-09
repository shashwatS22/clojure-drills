(defn make-counter []
  (let [n (atom 0)]
    #(swap! n inc)))
(let [c (make-counter)]
  (println (c))
  (println (c))
  (println (c)))
