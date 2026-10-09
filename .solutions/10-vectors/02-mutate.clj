(let [arr [2 3]
      a (conj (conj arr 4) 1)
      b (pop (pop a))]
  (println (clojure.string/join " " a))
  (println (clojure.string/join " " b)))
