(require '[clojure.test :refer [deftest is]])

(deftest fib-test
  (is (= (fib 0) 0))
  (is (= (fib 6) 8)))
