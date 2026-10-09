(let [arr [10 9 100 2]]
  (println (clojure.string/join " " (sort arr)))
  (println (clojure.string/join " " (sort > arr))))
