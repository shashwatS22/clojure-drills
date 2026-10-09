(def sample-request {:request-method :get :uri "/" :headers {}})
(defn wrap-log [handler]
  (fn [req]
    (println "hit")
    (handler req)))
(defn handler [_] {:status 200 :headers {} :body "ok"})
(println (:body ((wrap-log handler) sample-request)))
