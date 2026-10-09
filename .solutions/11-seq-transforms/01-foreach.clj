(let [arr [10 20 30]]
  (doseq [[i v] (map-indexed vector arr)] (println (str i ": " v))))
