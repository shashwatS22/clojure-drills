(let [n 1223334444 s (str n) freqs (frequencies s)]
  (println (clojure.string/join " " (map (fn [[d c]] (str d ":" c)) (sort freqs)))))
