(let [people [{:name "Ada" :age 36 :city "London"}
 {:name "Raman" :age 42 :city "Kolkata"}
 {:name "Meera" :age 29 :city "Pune"}]]
  (doseq [p people] (println (:name p))))
