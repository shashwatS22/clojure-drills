(require '[clojure.test :refer [deftest is]])

(deftest is-even-test
  (is (is-even 4))
  (is (not (is-even 7))))
