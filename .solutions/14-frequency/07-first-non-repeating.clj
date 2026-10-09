(let [s "swiss" freqs (frequencies s)]
  (println (or (first (filter #(= 1 (freqs %)) s)) "none")))
