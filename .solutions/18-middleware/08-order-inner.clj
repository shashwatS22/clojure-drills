(def sample-request {:request-method :get :uri "/" :headers {}})
(defn wrap-tag [label]
  (fn [handler]
    (fn [req]
      (let [resp (handler req)]
        (update resp :trace conj label)))))
(defn base [_] {:status 200 :headers {} :body "ok" :trace []})
(def app ((wrap-tag "A") ((wrap-tag "B") base)))
(println (clojure.string/join " " (:trace (app sample-request))))
