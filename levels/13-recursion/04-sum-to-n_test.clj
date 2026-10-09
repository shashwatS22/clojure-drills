(require '[clojure.test :refer [deftest is]])

(deftest sum-to-test
  (is (= (sum-to 5) 15))
  (is (= (sum-to 1) 1)))
