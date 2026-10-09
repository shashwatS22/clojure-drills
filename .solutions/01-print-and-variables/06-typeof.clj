(defn type-label [x]
  (cond
    (number? x) "number"
    (string? x) "string"
    (boolean? x) "boolean"
    (nil? x) "nil"
    (map? x) "map"
    :else "other"))
(doseq [v [5 "hi" true nil nil {}]]
  (println (type-label v)))
