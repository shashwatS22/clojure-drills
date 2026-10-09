(let [p (promise)]
  (future (deliver p "done"))
  (println @p))
