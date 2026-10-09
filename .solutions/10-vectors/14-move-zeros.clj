(let [arr [0 1 0 3 12]]
  (println (clojure.string/join " " (concat (remove zero? arr) (repeat (count (filter zero? arr)) 0)))))
