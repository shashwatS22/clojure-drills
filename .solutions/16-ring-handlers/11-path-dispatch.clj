(def items-request {:request-method :get :uri "/items" :headers {}})
(require '[ring.util.response :refer [response not-found]])
(defn handler [req]
  (case (:uri req)
    "/users" (response "users")
    "/items" (response "items")
    (not-found req)))
(let [resp (handler items-request)]
  (println (:status resp))
  (println (:body resp)))
