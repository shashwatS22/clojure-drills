(let [s "programming"]
  (println (apply str (reduce (fn [acc ch] (if (some #{ch} acc) acc (conj acc ch))) [] s))))
