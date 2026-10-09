(def sample-request {:request-method :get :uri "/search?q=clojure" :headers {}})
(require '[compojure.core :refer [GET routes]]
            '[ring.middleware.params :refer [wrap-params]]
            '[ring.util.response :refer [response]])
(def app (-> (routes (GET "/search" {params :params} (response (get params "q"))))
             wrap-params))
(println (:body (app sample-request)))
