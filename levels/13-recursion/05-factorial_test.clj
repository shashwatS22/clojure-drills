(require '[clojure.test :refer [deftest is]])

(deftest factorial-test
  (is (= (factorial 5) 120))
  (is (= (factorial 0) 1)))
