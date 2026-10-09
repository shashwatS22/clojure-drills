(try
  (throw (ex-info "failed" {:status 500}))
  (catch Exception e
    (println (ex-message e))
    (println (:status (ex-data e)))))
