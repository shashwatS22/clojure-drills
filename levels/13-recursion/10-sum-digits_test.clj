(require '[clojure.test :refer [deftest is]])

(deftest sum-digits-test
  (is (= (sum-digits 123) 6)))
