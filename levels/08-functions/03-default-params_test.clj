(require '[clojure.test :refer [deftest is]])

(deftest greet-test
  (is (= (greet "Ada") "Hello, Ada!"))
  (is (= (greet "Ada" "Hi") "Hi, Ada!")))
