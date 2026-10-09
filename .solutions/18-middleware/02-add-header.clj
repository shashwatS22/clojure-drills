(def sample-request {:request-method :get :uri "/" :headers {}})
(defn wrap-trace [handler]
  (fn [req]
    (-> (handler req)
        (update :headers assoc "X-Trace" "1"))))
(defn handler [_] {:status 200 :headers {} :body "ok"})
(println (get-in ((wrap-trace handler) sample-request) [:headers "X-Trace"]))
