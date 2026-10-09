(require '[ring.util.response :refer [response status]])
(let [resp (-> (response "created") (status 201))]
  (println (:status resp))
  (println (:body resp)))
