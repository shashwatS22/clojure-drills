(defn repeat-callback [times f]
  (doseq [i (range times)] (f i)))
(repeat-callback 3 #(println "step" %))
