(let [arr [7 3 9 1] target 9]
  (println (first (keep-indexed #(when (= %2 target) %1) arr))))
