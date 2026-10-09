(let [user (-> {:name "Ada" :age 36}
                 (assoc :city "London")
                 (update :age inc)
                 (dissoc :age))]
  (println (clojure.string/join " " (sort (keys user)))))
