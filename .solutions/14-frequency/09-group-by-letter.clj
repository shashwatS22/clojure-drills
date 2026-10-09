(let [words ["apple" "avocado" "banana" "blueberry" "cherry"]
      groups (group-by #(first %) words)]
  (doseq [k (sort groups)]
    (println (str k ": " (clojure.string/join ", " (groups k))))))
