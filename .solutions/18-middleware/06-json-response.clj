(def sample-request {:request-method :get :uri "/" :headers {}})
(require '[cheshire.core :as json]
            '[ring.util.response :refer [response content-type]])
(defn wrap-json-response [handler]
  (fn [req]
    (let [resp (handler req)]
      (if (map? (:body resp))
        (-> resp
            (update :body json/generate-string)
            (content-type "application/json"))
        resp))))
(defn handler [_] {:status 200 :headers {} :body {:a 1}})
(println (:body ((wrap-json-response handler) sample-request)))
