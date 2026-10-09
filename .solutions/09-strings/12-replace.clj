(require '[clojure.string :as str])
(let [s "cat bat cat"]
  (println (str/replace-first s "cat" "dog"))
  (println (str/replace s "cat" "dog")))
