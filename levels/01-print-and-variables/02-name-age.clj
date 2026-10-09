;; 01-print-and-variables / 02-name-age
;;
;; TASK
;; GIVEN name = "Riya", age = 27. Print `Riya is 27 years old`.
;;
;; HINT
;; println can take several arguments; Clojure prints them separated by
;; spaces. Use the GIVEN name and age bindings.
;;
;; DO NOT CHANGE the GIVEN values.
;;
;; EXPECTED OUTPUT
;; Riya is 27 years old
;;
;; ---- GIVEN ----
(def name "Riya")
(def age 27)
;; ---------------
;;
;; Your code below
(println name "is" age "years old")