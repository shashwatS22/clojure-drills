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

(defn body-string [req]
  (let [b (:body req)]
    (cond (string? b) b
          (instance? java.io.InputStream b) (slurp b)
          :else (str b))))

(require '[ring.adapter.jetty :refer [run-jetty]]
         '[compojure.core :refer [POST routes]]
         '[ring.util.response :refer [response]]
         '[cheshire.core :as json])
(let [app (routes (POST "/double" req
                        (let [n (:x (json/parse-string (body-string req) true))]
                          (response (str (* 2 n))))))
      server (run-jetty app {:port 0 :join? false})]
  (try
    (println (:body (http-post-json (server-port server) "/double" "{\"x\":2}")))
    (finally (.stop server))))
