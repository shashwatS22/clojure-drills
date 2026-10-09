(require '[clojure.test :refer [deftest is]])

(deftest apply-twice-test
  (is (= (apply-twice inc 3) 5)))
