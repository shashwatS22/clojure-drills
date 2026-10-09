(require '[clojure.string :as str])
(let [s "hello world" letters (filter #(Character/isLetter %) s)]
  (let [v (count (filter #(#{\a \e \i \o \u} (Character/toLowerCase %)) letters))]
    (println "vowels:" v)
    (println "consonants:" (- (count letters) v))))
