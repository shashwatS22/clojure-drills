(def sample-request {:request-method :post :uri "/echo" :headers {} :body "hi"})
(require '[compojure.core :refer [POST routes]]
            '[ring.util.response :refer [response]])
(def app (routes (POST "/echo" req (response (:body req)))))
(println (:body (app sample-request)))
