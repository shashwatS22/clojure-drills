(let [arr (range 1 11)]
  (println (clojure.string/join " " (filter even? arr))))
