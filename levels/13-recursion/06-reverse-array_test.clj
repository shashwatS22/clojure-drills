(require '[clojure.test :refer [deftest is]])

(deftest reverse-test
  (is (= (reverse-array ["a" "b" "c"]) ["c" "b" "a"])))
