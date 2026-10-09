(let [s "banana" freqs (reduce (fn [m ch] (update m ch (fnil inc 0))) {} s) order (distinct s)]
  (println (clojure.string/join " " (map #(str % ":" (freqs %)) order))))
