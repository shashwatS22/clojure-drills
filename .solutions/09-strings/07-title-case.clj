(require '[clojure.string :as str])
(let [s "learning javascript today"]
  (println (str/join " " (map str/capitalize (str/split s #"\s+")))))
