(require '[clojure.test :refer [deftest is]])

(deftest min-max-test
  (is (= (min-max [3 1 9]) {:min 1 :max 9})))
