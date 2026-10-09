(println "first")
(def f (future (println "third")))
(println "second")
@f
