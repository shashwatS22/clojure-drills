(let [defaults {:theme "light" :font-size 14}
      custom {:font-size 18}
      merged (merge defaults custom)]
  (println (:theme merged))
  (println (:font-size merged)))
