(require '[clojure.test :refer [deftest is]])

(deftest power-test
  (is (= (power 2 10) 1024)))
