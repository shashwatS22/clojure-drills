(def sample-request {:request-method :get :uri "/z" :headers {}})
(require '[compojure.core :refer [GET routes]]
            '[ring.util.response :refer [response]])
(def app (routes (GET "/a" [] (response "a"))))
(println (:status (app sample-request)))
