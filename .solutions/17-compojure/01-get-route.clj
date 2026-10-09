(def sample-request {:request-method :get :uri "/ping" :headers {}})
(require '[compojure.core :refer [GET routes]]
            '[ring.util.response :refer [response]])
(def app (routes (GET "/ping" [] (response "pong"))))
(println (:body (app sample-request)))
