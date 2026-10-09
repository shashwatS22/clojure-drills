;; 02-operators / 03-post-vs-pre
;;
;; TASK
;; GIVEN x = 5. Simulate post-increment and pre-increment using inc and
;; let (print values like JS x++/++x).
;;
;; HINT
;; There is no ++. Simulate with inc inside let: print x, then bind x to
;; (inc x) and print again.
;;
;; DO NOT CHANGE the GIVEN values.
;;
;; EXPECTED OUTPUT
;; 5
;; 6
;; 7
;; 7
;;
;; ---- GIVEN ----
(def x 5)
;; ---------------
;;
;; Your code below
