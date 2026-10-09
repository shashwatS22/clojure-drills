(let [arr [1 2 3 4 5]
      rev (loop [i (dec (count arr)) acc []]
        (if (neg? i) acc (recur (dec i) (conj acc (arr i)))))]
  (println (clojure.string/join " " rev)))
