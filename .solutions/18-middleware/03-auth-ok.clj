(def sample-request {:request-method :get :uri "/" :headers {"x-token" "open"}})
(require '[ring.util.response :refer [response status]])
(defn wrap-auth [handler]
  (fn [req]
    (if (= "open" (get-in req [:headers "x-token"]))
      (handler req)
      (-> (response "denied") (status 401)))))
(defn handler [_] (response "secret"))
(let [resp ((wrap-auth handler) sample-request)]
  (println (:status resp))
  (println (:body resp)))
