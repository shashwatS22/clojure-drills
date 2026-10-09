(def sample-request {:request-method :get :uri "/api" :headers {}})
(let [req sample-request]
  (println (name (:request-method req)))
  (println (:uri req)))
