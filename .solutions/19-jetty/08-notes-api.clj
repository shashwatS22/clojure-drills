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
         '[compojure.core :refer [GET POST routes]]
         '[ring.util.response :refer [response status]]
         '[cheshire.core :as json])
(def notes (atom []))
(let [app (routes
           (POST "/notes" req
             (let [title (:title (json/parse-string (body-string req) true))]
               (swap! notes conj {:title title})
               (status (response "") 201)))
           (GET "/notes" []
             (response (json/generate-string @notes))))
      server (run-jetty app {:port 0 :join? false})]
  (try
    (let [port (server-port server)
          post (http-post-json port "/notes" "{\"title\":\"a\"}")
          get-resp (http-get port "/notes")]
      (println (:status post))
      (println (count (json/parse-string (:body get-resp) true))))
    (finally (.stop server))))
