(let [arr [1 2 3 4]]
  (println (clojure.string/join " " (map #(* 2 %) arr))))
