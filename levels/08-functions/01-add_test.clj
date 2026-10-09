(require '[clojure.test :refer [deftest is]])

(deftest add-test
  (is (= (add 2 3) 5))
  (is (= (add -1 1) 0)))
