(require '[ring.util.response :refer [response status content-type header not-found redirect]])

(println (get-in (content-type (response "x") "text/plain") [:headers "Content-Type"]))
(let [r (not-found {})]
  (println (:status r))
  (println (:body r)))
(let [r (redirect "/home")]
  (println (:status r))
  (println (get-in r [:headers "Location"])))
