(let [a 12 b 4 op "/"]
  (println (case op "+" (+ a b) "-" (- a b) "*" (* a b) "/" (/ a b) "unknown")))
