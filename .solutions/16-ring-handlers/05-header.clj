(require '[ring.util.response :refer [response header]])
(println (get-in (header (response "x") "X-App" "drills") [:headers "X-App"]))
