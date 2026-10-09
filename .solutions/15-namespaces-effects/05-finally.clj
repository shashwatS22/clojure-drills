(try
  (try
    (println "try ok")
    (throw (ex-info "fail" {}))
    (finally (println "finally")))
  (catch Exception _
    (println "caught"))
  (finally (println "finally")))
