(require '[clojure.test :refer [deftest is]])

(deftest multiply-test
  (is (= (multiply 3 4) 12))
  (is (= (multiply -2 5) -10)))
