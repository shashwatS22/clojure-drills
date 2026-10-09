(let [a 3 b 4 c 8]
  (println (if (and (> (+ a b) c) (> (+ b c) a) (> (+ c a) b)) "valid" "invalid")))
