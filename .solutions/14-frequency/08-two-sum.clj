(let [arr [2 7 11 15] target 9 seen {}]
  (loop [i 0 m {}]
    (if (= i (count arr)) nil
      (let [x (nth arr i) need (- target x)]
        (if (contains? m need) (do (println (str (get m need) " " i)) nil)
          (recur (inc i) (assoc m x i)))))))
