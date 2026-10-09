;; 18-middleware / 05-json-body
;;
;; TASK
;; Parse JSON body field n.
;;
;; HINT
;; cheshire parse-string
;;
;; DO NOT CHANGE the GIVEN values.
;;
;; EXPECTED OUTPUT
;; 6
;;
;; ---- GIVEN ----
(def sample-request {:request-method :post :uri "/" :headers {"content-type" "application/json"} :body "{\"n\":3}"})
;; ---------------
;;
;; Your code below
