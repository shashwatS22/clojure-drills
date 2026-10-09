(let [scores {:math 90 :science 85 :art 72}]
  (doseq [[k v] scores] (println (str (name k) ": " v))))
