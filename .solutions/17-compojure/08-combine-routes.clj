(def sample-request {:request-method :get :uri "/b" :headers {}})
(require '[compojure.core :refer [GET routes defroutes]]
            '[ring.util.response :refer [response]])
(def r1 (routes (GET "/a" [] (response "first"))))
(def r2 (routes (GET "/b" [] (response "second"))))
(def app (routes r1 r2))
(println (:body (app sample-request)))
