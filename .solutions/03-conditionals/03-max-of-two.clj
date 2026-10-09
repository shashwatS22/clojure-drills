(let [a 34 b 34]
  (cond
    (> a b) (println a)
    (> b a) (println b)
    :else (println "equal")))
