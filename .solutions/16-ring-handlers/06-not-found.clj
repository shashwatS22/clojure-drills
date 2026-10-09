(require '[ring.util.response :refer [not-found]])
(let [resp (not-found {})]
  (println (:status resp))
  (println (:body resp)))
