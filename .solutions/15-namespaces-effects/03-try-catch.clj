(try
  (read-string "not json")
  (catch Exception _
    (println "caught an error")))
(println "still running")
