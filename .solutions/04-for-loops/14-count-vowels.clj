(let [s "javascript is fun"]
  (loop [chars (seq s) c 0]
    (if (empty? chars) (println c)
      (let [ch (first chars)]
        (recur (rest chars) (if (#{\a \e \i \o \u} ch) (inc c) c))))))
