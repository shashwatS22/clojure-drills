(require '[ring.util.response :refer [response]]
         '[compojure.core :refer [GET routes]]
         '[ring.adapter.jetty :refer [run-jetty]])

(println (:body ((routes (GET "/ping" [] (response "pong"))) {:request-method :get :uri "/ping"})))

(let [server (run-jetty (constantly (response "ok")) {:port 0 :join? false})]
  (println "started")
  (.stop server))
