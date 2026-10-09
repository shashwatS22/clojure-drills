(require '[clojure.string :as str])
(let [s " the quick  brown fox "]
  (println (count (str/split (str/trim s) #"\s+"))))
