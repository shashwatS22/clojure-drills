(def sample-request {:request-method :post :uri "/" :headers {"content-type" "application/json"} :body "{\"n\":3}"})
(require '[cheshire.core :as json]
            '[ring.util.response :refer [response]])
(defn wrap-json-body [handler]
  (fn [req]
    (let [body (when (:body req) (json/parse-string (:body req) true))]
      (handler (assoc req :json body)))))
(defn handler [req] (response (str (* 2 (:n (:json req))))))
(println (:body ((wrap-json-body handler) sample-request)))
