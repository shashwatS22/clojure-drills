(require '[clojure.test :refer [deftest is]])

(deftest sum-test
  (is (= (sum) 0))
  (is (= (sum 1 2 3) 6)))
