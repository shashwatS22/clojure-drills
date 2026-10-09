(require '[clojure.test :refer [deftest is]])

(deftest make-multiplier-test
  (let [double (make-multiplier 2)]
    (is (= (double 5) 10))))
