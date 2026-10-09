(require '[ring.util.response :refer [response]])
(let [resp (response "hello")]
  (println (:status resp))
  (println (:body resp)))
