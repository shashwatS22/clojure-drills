(let [arr [1 2 3 4 5] n (count arr)]
  (println (clojure.string/join " " (concat (subvec arr 1 n) [(arr 0)]))))
