(let [user {:address {:city "Bareilly"}}]
  (println (get-in user [:address :city])))
