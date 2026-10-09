(defn reverse-array [v]
  (loop [i (dec (count v)) acc []]
    (if (neg? i) acc (recur (dec i) (conj acc (v i))))))
