(require '[clojure.set :as set]
         '[clojure.string :as str])
(let [a [1 2 3 4] b [3 4 5]]
  (println (str/join " " (sort (set/union (set a) (set b)))))
  (println (str/join " " (sort (set/intersection (set a) (set b))))))
