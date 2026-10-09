;; 18-middleware / 03-auth-ok
;;
;; TASK
;; Valid x-token.
;;
;; HINT
;; check header
;;
;; DO NOT CHANGE the GIVEN values.
;;
;; EXPECTED OUTPUT
;; 200
;; secret
;;
;; ---- GIVEN ----
(def sample-request {:request-method :get :uri "/" :headers {"x-token" "open"}})
;; ---------------
;;
;; Your code below
