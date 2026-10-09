(require '[clojure.string :as str])
(let [s "  7  " t (str/trim s)]
  (println t)
  (println (format "%05d" (parse-long t))))
