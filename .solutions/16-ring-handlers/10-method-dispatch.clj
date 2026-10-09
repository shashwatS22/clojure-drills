(def health-request {:request-method :get :uri "/health" :headers {}})
(require '[ring.util.response :refer [response not-found]])
(defn handler [req]
  (if (and (= :get (:request-method req)) (= "/health" (:uri req)))
    (response "up")
    (not-found req)))
(let [resp (handler health-request)]
  (println (:status resp))
  (println (:body resp)))
