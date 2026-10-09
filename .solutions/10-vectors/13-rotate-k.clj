(let [arr [1 2 3 4 5 6 7] k 3 n (count arr) k (mod k n)]
  (println (clojure.string/join " " (concat (subvec arr k n) (subvec arr 0 k)))))
