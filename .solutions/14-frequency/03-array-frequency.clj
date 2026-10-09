(let [arr [10 5 10 15 10 5] freqs (frequencies arr) order (distinct arr)]
  (println (clojure.string/join " " (map #(str % ":" (freqs %)) order))))
