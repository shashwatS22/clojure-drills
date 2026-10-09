;; 01-print-and-variables / 05-let-reassign
;;
;; TASK
;; Print count 10 then 20 using let shadowing (no reassignment).
;;
;; HINT
;; let bindings cannot be reassigned. Nest an inner let that binds the
;; same name to a new value (shadowing).
;;
;; EXPECTED OUTPUT
;; 10
;; 20
;;
;; Your code below

(let [count 10]
(println count)
(let [count 20]
(println count)
))
