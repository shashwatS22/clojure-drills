(let [marks 73]
  (cond
    (>= marks 90) (println "A")
    (>= marks 75) (println "B")
    (>= marks 60) (println "C")
    (>= marks 40) (println "D")
    :else (println "F")))
