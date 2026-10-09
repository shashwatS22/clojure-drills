(def sample-request {:request-method :get :uri "/" :headers {"authorization" "Bearer secret"}})
(println (get-in sample-request [:headers "authorization"]))
