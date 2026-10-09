(let [s "bareilly"]
  (loop [chars (seq s) out ""]
    (if (empty? chars) (println out)
      (recur (rest chars) (str (first chars) out)))))
