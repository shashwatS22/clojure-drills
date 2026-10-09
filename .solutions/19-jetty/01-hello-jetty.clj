(require '[hato.client :as http])

(defn server-port [server]
  (-> server .getConnectors first .getLocalPort))

(defn http-get [port path]
  (let [url (str "http://127.0.0.1:" port path)
        resp (http/get url {:as :string :throw-exceptions false})]
    {:status (:status resp) :body (:body resp)}))

(defn http-post-json [port path json-body]
  (let [url (str "http://127.0.0.1:" port path)
        resp (http/post url {:body json-body
                              :headers {"Content-Type" "application/json"}
                              :as :string
                              :throw-exceptions false})]
    {:status (:status resp) :body (:body resp)}))

(require '[ring.adapter.jetty :refer [run-jetty]]
         '[ring.util.response :refer [response]])
(let [app (constantly (response "hello"))
      server (run-jetty app {:port 0 :join? false})]
  (try
    (println (:body (http-get (server-port server) "/")))
    (finally (.stop server))))
