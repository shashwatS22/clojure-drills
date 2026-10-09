(let [people [{:name "Ada" :age 36 :city "London"}
 {:name "Raman" :age 42 :city "Kolkata"}
 {:name "Meera" :age 29 :city "Pune"}]]
  (println (clojure.string/join " " (map :name (sort-by :age people)))))
