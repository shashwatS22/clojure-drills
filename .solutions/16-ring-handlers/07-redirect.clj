(require '[ring.util.response :refer [redirect]])
(let [resp (redirect "/home")]
  (println (:status resp))
  (println (get-in resp [:headers "Location"])))
