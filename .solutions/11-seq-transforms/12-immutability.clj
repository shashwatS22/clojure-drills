(let [arr [1 2 3] mapped (map #(* 2 %) arr)]
  (println (clojure.string/join " " mapped))
  (println (clojure.string/join " " arr)))
