(require '[clojure.string :as str])
(let [f1 (future (do (Thread/sleep 5) 1))
      f2 (future (do (Thread/sleep 10) 2))
      f3 (future (do (Thread/sleep 15) 3))]
  (println (str/join " " [@f1 @f2 @f3])))
