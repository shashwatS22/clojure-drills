(require '[clojure.test :refer [deftest is]])

(deftest pal-test
  (is (is-palindrome "racecar"))
  (is (not (is-palindrome "abc"))))
