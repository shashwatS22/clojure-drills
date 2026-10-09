(let [ch "u"]
  (println (if (#{\a \e \i \o \u} (first ch)) "vowel" "consonant")))
