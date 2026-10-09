(require '[clojure.string :as str])
(let [s "a,b,c,d"]
  (println (str/join " - " (str/split s #","))))
