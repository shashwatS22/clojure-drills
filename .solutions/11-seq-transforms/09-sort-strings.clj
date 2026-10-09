(require '[clojure.string :as str])
(let [arr ["banana" "apple" "cherry"]]
  (println (str/join " " (sort arr))))
