(def sample-request {:request-method :get :uri "/items/7" :headers {}})
(require '[compojure.core :refer [GET routes]]
            '[ring.util.response :refer [response content-type]]
            '[cheshire.core :as json])
(def app (routes (GET "/items/:id" [id] (-> (response (json/generate-string {:id (Long/parseLong id)}))
                                            (content-type "application/json")))))
(println (:body (app sample-request)))
