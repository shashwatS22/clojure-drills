(def sample-request {:request-method :get :uri "/users/42" :headers {}})
(require '[compojure.core :refer [GET routes]]
            '[ring.util.response :refer [response]])
(def app (routes (GET "/users/:id" [id] (response (str "user-" id)))))
(println (:body (app sample-request)))
