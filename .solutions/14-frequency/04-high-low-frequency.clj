(let [arr [10 5 10 15 10 5] freqs (frequencies arr)]
  (let [[hi _] (apply max-key val freqs)
        [lo _] (apply min-key val freqs)]
    (println "highest:" hi)
    (println "lowest:" lo)))
