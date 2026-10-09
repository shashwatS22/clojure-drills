(println "not yet")
(def d (delay (do (println "computing") "done")))
(println @d)
(println @d)
