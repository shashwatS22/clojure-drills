#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def format_given(given: str) -> str:
    g = (given or "").strip()
    if not g:
        return ""
    if g.startswith("(def"):
        return g
    if g.startswith("def "):
        return f"({g})"
    return g

def stub(level, base, task, hint, given, expected):
    lines = expected.split("\n")
    exp_comment = "\n".join(f";; {l}" if l else ";;" for l in lines)
    given_block = given.strip()
    if given_block:
        given_block = given_block + "\n"
    return f""";; {level} / {base}
;;
;; TASK
;; {task}
;;
;; HINT
;; {hint}
;;
;; DO NOT CHANGE the GIVEN values.
;;
;; EXPECTED OUTPUT
{exp_comment}
;;
;; ---- GIVEN ----
{given_block};; ---------------
;;
;; Your code below
"""

def write_ex(level, base, task, hint, given, expected, solution):
    given_fmt = format_given(given)
    sol_text = (given_fmt + "\n" + solution.strip()).strip() + "\n" if given_fmt else solution.strip() + "\n"
    for folder in ("levels", "stubs"):
        d = ROOT / folder / level
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{base}.clj").write_text(stub(level, base, task, hint, given_fmt, expected))
    sol_d = ROOT / ".solutions" / level
    sol_d.mkdir(parents=True, exist_ok=True)
    (sol_d / f"{base}.clj").write_text(sol_text)

L16 = "16-ring-handlers"
L17 = "17-compojure"
L18 = "18-middleware"
L19 = "19-jetty"

# Level 16
write_ex(L16, "01-response-map", "Build response map; print status and body.", "Map with :status :headers :body.", "", "200\nok",
"""(let [resp {:status 200 :headers {} :body "ok"}]
  (println (:status resp))
  (println (:body resp)))""")

write_ex(L16, "02-ring-response", "Use (response \"hello\").", "ring.util.response", "", "200\nhello",
"""(require '[ring.util.response :refer [response]])
(let [resp (response "hello")]
  (println (:status resp))
  (println (:body resp)))""")

write_ex(L16, "03-status-code", "Return 201 with status helper.", "-> threading macro", "", "201\ncreated",
"""(require '[ring.util.response :refer [response status]])
(let [resp (-> (response "created") (status 201))]
  (println (:status resp))
  (println (:body resp)))""")

write_ex(L16, "04-content-type", "Set text/plain content type.", "content-type function", "", "text/plain",
"""(require '[ring.util.response :refer [response content-type]])
(println (get-in (content-type (response "x") "text/plain") [:headers "Content-Type"]))""")

write_ex(L16, "05-header", "Add X-App header.", "header helper", "", "drills",
"""(require '[ring.util.response :refer [response header]])
(println (get-in (header (response "x") "X-App" "drills") [:headers "X-App"]))""")

write_ex(L16, "06-not-found", "Call not-found.", "(not-found {})", "", "404\n{}",
"""(require '[ring.util.response :refer [not-found]])
(let [resp (not-found {})]
  (println (:status resp))
  (println (:body resp)))""")

write_ex(L16, "07-redirect", "Redirect to /home.", "redirect fn", "", "302\n/home",
"""(require '[ring.util.response :refer [redirect]])
(let [resp (redirect "/home")]
  (println (:status resp))
  (println (get-in resp [:headers "Location"])))""")

write_ex(L16, "08-read-request", "Print method and uri.", "name on keyword", "def sample-request {:request-method :get :uri \"/api\" :headers {}}", "get\n/api",
"""(let [req sample-request]
  (println (name (:request-method req)))
  (println (:uri req)))""")

write_ex(L16, "09-read-header", "Print authorization header.", "lower-case keys", 'def sample-request {:request-method :get :uri "/" :headers {"authorization" "Bearer secret"}}', "Bearer secret",
"""(println (get-in sample-request [:headers "authorization"]))""")

write_ex(L16, "10-method-dispatch", "GET /health -> up.", "handler fn", "def health-request {:request-method :get :uri \"/health\" :headers {}}", "200\nup",
"""(require '[ring.util.response :refer [response not-found]])
(defn handler [req]
  (if (and (= :get (:request-method req)) (= "/health" (:uri req)))
    (response "up")
    (not-found req)))
(let [resp (handler health-request)]
  (println (:status resp))
  (println (:body resp)))""")

write_ex(L16, "11-path-dispatch", "Dispatch /items.", "case on :uri", "def items-request {:request-method :get :uri \"/items\" :headers {}}", "200\nitems",
"""(require '[ring.util.response :refer [response not-found]])
(defn handler [req]
  (case (:uri req)
    "/users" (response "users")
    "/items" (response "items")
    (not-found req)))
(let [resp (handler items-request)]
  (println (:status resp))
  (println (:body resp)))""")

write_ex(L16, "12-json-body", "JSON body {\"ok\":true}.", "Cheshire + content-type", "def any-request {:request-method :get :uri \"/\" :headers {}}", '200\n{"ok":true}',
"""(require '[ring.util.response :refer [response content-type]]
            '[cheshire.core :as json])
(defn handler [_]
  (-> (response (json/generate-string {:ok true}))
      (content-type "application/json")))
(let [resp (handler any-request)]
  (println (:status resp))
  (println (:body resp)))""")

# Level 17 - compojure (clojure CLI)
write_ex(L17, "01-get-route", "GET /ping -> pong.", "defroutes + routes", "def sample-request {:request-method :get :uri \"/ping\" :headers {}}", "pong",
"""(require '[compojure.core :refer [GET routes]]
            '[ring.util.response :refer [response]])
(def app (routes (GET "/ping" [] (response "pong"))))
(println (:body (app sample-request)))""")

write_ex(L17, "02-post-route", "POST /echo returns body.", "POST route", 'def sample-request {:request-method :post :uri "/echo" :headers {} :body "hi"}', "hi",
"""(require '[compojure.core :refer [POST routes]]
            '[ring.util.response :refer [response]])
(def app (routes (POST "/echo" req (response (:body req)))))
(println (:body (app sample-request)))""")

write_ex(L17, "03-path-param", "GET /users/:id.", "id in route vector", 'def sample-request {:request-method :get :uri "/users/42" :headers {}}', "user-42",
"""(require '[compojure.core :refer [GET routes]]
            '[ring.util.response :refer [response]])
(def app (routes (GET "/users/:id" [id] (response (str "user-" id)))))
(println (:body (app sample-request)))""")

write_ex(L17, "04-query-param", "GET /search?q=clojure with wrap-params.", "ring.middleware.params", 'def sample-request {:request-method :get :uri "/search?q=clojure" :headers {}}', "clojure",
"""(require '[compojure.core :refer [GET routes]]
            '[ring.middleware.params :refer [wrap-params]]
            '[ring.util.response :refer [response]])
(def app (-> (routes (GET "/search" {params :params} (response (get params "q"))))
             wrap-params))
(println (:body (app sample-request)))""")

write_ex(L17, "05-keyword-params", "wrap-keyword-params for :q.", "ring.middleware.keyword-params", 'def sample-request {:request-method :get :uri "/search?q=clojure" :headers {}}', "clojure",
"""(require '[compojure.core :refer [GET routes]]
            '[ring.middleware.params :refer [wrap-params]]
            '[ring.middleware.keyword-params :refer [wrap-keyword-params]]
            '[ring.util.response :refer [response]])
(def app (-> (routes (GET "/search" {params :params} (response (:q params))))
             wrap-params
             wrap-keyword-params))
(println (:body (app sample-request)))""")

write_ex(L17, "06-not-found-route", "Unknown path -> 404.", "only /a defined", 'def sample-request {:request-method :get :uri "/z" :headers {}}', "404",
"""(require '[compojure.core :refer [GET routes]]
            '[ring.util.response :refer [response]])
(def app (routes (GET "/a" [] (response "a"))))
(println (:status (app sample-request)))""")

write_ex(L17, "07-context", "Context /api prefix.", "context macro", 'def sample-request {:request-method :get :uri "/api/v1" :headers {}}', "v1",
"""(require '[compojure.core :refer [GET context routes]]
            '[ring.util.response :refer [response]])
(def app (routes (context "/api" [] (GET "/v1" [] (response "v1")))))
(println (:body (app sample-request)))""")

write_ex(L17, "08-combine-routes", "Combine two route tables.", "routes merges", 'def sample-request {:request-method :get :uri "/b" :headers {}}', "second",
"""(require '[compojure.core :refer [GET routes defroutes]]
            '[ring.util.response :refer [response]])
(def r1 (routes (GET "/a" [] (response "first"))))
(def r2 (routes (GET "/b" [] (response "second"))))
(def app (routes r1 r2))
(println (:body (app sample-request)))""")

write_ex(L17, "09-json-item", "JSON item by id.", "Cheshire in response", 'def sample-request {:request-method :get :uri "/items/7" :headers {}}', '{"id":7}',
"""(require '[compojure.core :refer [GET routes]]
            '[ring.util.response :refer [response content-type]]
            '[cheshire.core :as json])
(def app (routes (GET "/items/:id" [id] (-> (response (json/generate-string {:id (Long/parseLong id)}))
                                            (content-type "application/json")))))
(println (:body (app sample-request)))""")

write_ex(L17, "10-method-not-allowed", "POST to GET-only route.", "Compojure returns 404", 'def sample-request {:request-method :post :uri "/x" :headers {}}', "404",
"""(require '[compojure.core :refer [GET routes]]
            '[ring.util.response :refer [response]])
(def app (routes (GET "/x" [] (response "x"))))
(println (:status (app sample-request)))""")

# Level 18 middleware
write_ex(L18, "01-wrap-log", "Middleware prints hit.", "call handler after println", "def sample-request {:request-method :get :uri \"/\" :headers {}}", "hit\nok",
"""(defn wrap-log [handler]
  (fn [req]
    (println "hit")
    (handler req)))
(defn handler [_] {:status 200 :headers {} :body "ok"})
(println (:body ((wrap-log handler) sample-request)))""")

write_ex(L18, "02-add-header", "Add X-Trace 1.", "update :headers on response", "def sample-request {:request-method :get :uri \"/\" :headers {}}", "1",
"""(defn wrap-trace [handler]
  (fn [req]
    (-> (handler req)
        (update :headers assoc "X-Trace" "1"))))
(defn handler [_] {:status 200 :headers {} :body "ok"})
(println (get-in ((wrap-trace handler) sample-request) [:headers "X-Trace"]))""")

write_ex(L18, "03-auth-ok", "Valid x-token.", "check header", 'def sample-request {:request-method :get :uri "/" :headers {"x-token" "open"}}', "200\nsecret",
"""(require '[ring.util.response :refer [response status]])
(defn wrap-auth [handler]
  (fn [req]
    (if (= "open" (get-in req [:headers "x-token"]))
      (handler req)
      (-> (response "denied") (status 401)))))
(defn handler [_] (response "secret"))
(let [resp ((wrap-auth handler) sample-request)]
  (println (:status resp))
  (println (:body resp)))""")

write_ex(L18, "04-auth-fail", "Missing token -> 401.", "same middleware", 'def sample-request {:request-method :get :uri "/" :headers {}}', "401",
"""(require '[ring.util.response :refer [response status]])
(defn wrap-auth [handler]
  (fn [req]
    (if (= "open" (get-in req [:headers "x-token"]))
      (handler req)
      (-> (response "denied") (status 401)))))
(defn handler [_] (response "secret"))
(println (:status ((wrap-auth handler) sample-request)))""")

write_ex(L18, "05-json-body", "Parse JSON body field n.", "cheshire parse-string", 'def sample-request {:request-method :post :uri "/" :headers {"content-type" "application/json"} :body "{\\"n\\":3}"}', "6",
"""(require '[cheshire.core :as json]
            '[ring.util.response :refer [response]])
(defn wrap-json-body [handler]
  (fn [req]
    (let [body (when (:body req) (json/parse-string (:body req) true))]
      (handler (assoc req :json body)))))
(defn handler [req] (response (str (* 2 (:n (:json req))))))
(println (:body ((wrap-json-body handler) sample-request)))""")

write_ex(L18, "06-json-response", "Encode map as JSON body.", "cheshire generate-string", "def sample-request {:request-method :get :uri \"/\" :headers {}}", '{"a":1}',
"""(require '[cheshire.core :as json]
            '[ring.util.response :refer [response content-type]])
(defn wrap-json-response [handler]
  (fn [req]
    (let [resp (handler req)]
      (if (map? (:body resp))
        (-> resp
            (update :body json/generate-string)
            (content-type "application/json"))
        resp))))
(defn handler [_] {:status 200 :headers {} :body {:a 1}})
(println (:body ((wrap-json-response handler) sample-request)))""")

write_ex(L18, "07-order-outer", "Outer A inner B on response trace.", "Middleware stack order", "def sample-request {:request-method :get :uri \"/\" :headers {}}", "A B",
"""(defn wrap-tag [label]
  (fn [handler]
    (fn [req]
      (let [resp (handler req)]
        (update resp :trace conj label)))))
(defn base [_] {:status 200 :headers {} :body "ok" :trace []})
(def app ((wrap-tag "B") ((wrap-tag "A") base)))
(println (clojure.string/join " " (:trace (app sample-request))))""")

write_ex(L18, "08-order-inner", "Swap middleware order.", "Compare trace order", "def sample-request {:request-method :get :uri \"/\" :headers {}}", "B A",
"""(defn wrap-tag [label]
  (fn [handler]
    (fn [req]
      (let [resp (handler req)]
        (update resp :trace conj label)))))
(defn base [_] {:status 200 :headers {} :body "ok" :trace []})
(def app ((wrap-tag "A") ((wrap-tag "B") base)))
(println (clojure.string/join " " (:trace (app sample-request))))""")

BODY_STR = """
(defn body-string [req]
  (let [b (:body req)]
    (cond (string? b) b
          (instance? java.io.InputStream b) (slurp b)
          :else (str b))))
"""


JETTY = '''
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
'''

write_ex(L19, "01-hello-jetty", "Jetty GET / returns hello.", "run-jetty :join? false", "", "hello",
JETTY + """
(require '[ring.adapter.jetty :refer [run-jetty]]
         '[ring.util.response :refer [response]])
(let [app (constantly (response "hello"))
      server (run-jetty app {:port 0 :join? false})]
  (try
    (println (:body (http-get (server-port server) "/")))
    (finally (.stop server))))""")

write_ex(L19, "02-status-line", "Status 201 and body.", "status helper", "", "201\nmade",
JETTY + """
(require '[ring.adapter.jetty :refer [run-jetty]]
         '[ring.util.response :refer [response status]])
(let [app (constantly (-> (response "made") (status 201)))
      server (run-jetty app {:port 0 :join? false})]
  (try
    (let [{:keys [status body]} (http-get (server-port server) "/")]
      (println status)
      (println body))
    (finally (.stop server))))""")

write_ex(L19, "03-compojure-jetty", "Compojure on Jetty.", "GET /ping", "", "pong",
JETTY + """
(require '[ring.adapter.jetty :refer [run-jetty]]
         '[compojure.core :refer [GET routes]]
         '[ring.util.response :refer [response]])
(let [app (routes (GET "/ping" [] (response "pong")))
      server (run-jetty app {:port 0 :join? false})]
  (try
    (println (:body (http-get (server-port server) "/ping")))
    (finally (.stop server))))""")

write_ex(L19, "04-not-found-jetty", "404 on Jetty.", "explicit 404 response", "", "404",
JETTY + """
(require '[ring.adapter.jetty :refer [run-jetty]]
         '[ring.util.response :refer [response status]])
(let [app (constantly (-> (response "missing") (status 404)))
      server (run-jetty app {:port 0 :join? false})]
  (try
    (println (:status (http-get (server-port server) "/missing")))
    (finally (.stop server))))""")

write_ex(L19, "05-query-jetty", "Query param on Jetty.", "wrap-params", "", "jetty",
JETTY + """
(require '[ring.adapter.jetty :refer [run-jetty]]
         '[compojure.core :refer [GET routes]]
         '[ring.middleware.params :refer [wrap-params]]
         '[ring.util.response :refer [response]])
(let [app (-> (routes (GET "/echo" {params :params} (response (get params "q"))))
              wrap-params)
      server (run-jetty app {:port 0 :join? false})]
  (try
    (println (:body (http-get (server-port server) "/echo?q=jetty")))
    (finally (.stop server))))""")

write_ex(L19, "06-post-json-jetty", "POST JSON double.", "parse body string", "", "4",
JETTY + BODY_STR + """
(require '[ring.adapter.jetty :refer [run-jetty]]
         '[compojure.core :refer [POST routes]]
         '[ring.util.response :refer [response]]
         '[cheshire.core :as json])
(let [app (routes (POST "/double" req
                        (let [n (:x (json/parse-string (body-string req) true))]
                          (response (str (* 2 n))))))
      server (run-jetty app {:port 0 :join? false})]
  (try
    (println (:body (http-post-json (server-port server) "/double" "{\\"x\\":2}")))
    (finally (.stop server))))""")

write_ex(L19, "07-middleware-jetty", "Auth token on Jetty.", "x-token header", "", "ok",
JETTY + """
(require '[ring.adapter.jetty :refer [run-jetty]]
         '[ring.util.response :refer [response status]])
(defn wrap-token [handler]
  (fn [req]
    (if (= "yes" (get-in req [:headers "x-token"]))
      (handler req)
      (-> (response "no") (status 401)))))
(let [app (-> (constantly (response "ok")) wrap-token)
      server (run-jetty app {:port 0 :join? false})]
  (try
    (let [port (server-port server)
          resp (http/get (str "http://127.0.0.1:" port "/")
                         {:headers {"x-token" "yes"} :as :string :throw-exceptions false})]
      (println (:body resp)))
    (finally (.stop server))))""")

write_ex(L19, "08-notes-api", "In-memory notes API.", "POST then GET", "", "201\n1",
JETTY + BODY_STR + """
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
          post (http-post-json port "/notes" "{\\"title\\":\\"a\\"}")
          get-resp (http-get port "/notes")]
      (println (:status post))
      (println (count (json/parse-string (:body get-resp) true))))
    (finally (.stop server))))""")

print("Scaffolded levels 16-19")
