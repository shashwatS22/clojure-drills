(def any-request {:request-method :get :uri "/" :headers {}})
(require '[ring.util.response :refer [response content-type]]
            '[cheshire.core :as json])
(defn handler [_]
  (-> (response (json/generate-string {:ok true}))
      (content-type "application/json")))
(let [resp (handler any-request)]
  (println (:status resp))
  (println (:body resp)))
