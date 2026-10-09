(def sample-request {:request-method :post :uri "/x" :headers {}})
(require '[compojure.core :refer [GET routes]]
            '[ring.util.response :refer [response]])
(def app (routes (GET "/x" [] (response "x"))))
(println (:status (app sample-request)))
