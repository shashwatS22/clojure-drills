(let [age 17 is-citizen true]
  (println (if (and (>= age 18) is-citizen) "can vote" "cannot vote")))
