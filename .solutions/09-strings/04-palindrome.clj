(let [s "racecar"]
  (println (= s (apply str (reverse (seq s))))))
