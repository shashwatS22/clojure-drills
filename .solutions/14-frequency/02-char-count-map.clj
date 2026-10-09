(let [s "banana" f (frequencies s) order (distinct s)]
  (println (clojure.string/join " " (map #(str % ":" (f %)) order))))
