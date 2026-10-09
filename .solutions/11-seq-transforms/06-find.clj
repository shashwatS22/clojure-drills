(let [arr [3 8 12 5]]
  (println (first (filter #(> % 7) arr)))
  (println (first (keep-indexed #(when (> %2 7) %1) arr))))
