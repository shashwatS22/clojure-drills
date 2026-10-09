(require '[cheshire.core :as json])
(let [people [{:name "Ada" :age 36 :city "London"}]
      s (json/generate-string (first people))
      parsed (json/parse-string s true)]
  (println s)
  (println (:name parsed)))
