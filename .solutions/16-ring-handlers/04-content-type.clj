(require '[ring.util.response :refer [response content-type]])
(println (get-in (content-type (response "x") "text/plain") [:headers "Content-Type"]))
