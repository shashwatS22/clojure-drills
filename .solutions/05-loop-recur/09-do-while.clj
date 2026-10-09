(let [n 0]
  (println "ran once")
  (loop [once true]
    (when once
      (println "loop finished")
      (recur false))))
