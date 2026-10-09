(def sample-request {:request-method :get :uri "/api/v1" :headers {}})
(require '[compojure.core :refer [GET context routes]]
            '[ring.util.response :refer [response]])
(def app (routes (context "/api" [] (GET "/v1" [] (response "v1")))))
(println (:body (app sample-request)))
