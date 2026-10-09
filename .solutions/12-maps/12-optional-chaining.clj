(let [user {:name "Ada"}]
  (println (get-in user [:address :city]))
  (println (or (get-in user [:address :city]) "unknown")))
