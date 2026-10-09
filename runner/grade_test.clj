(ns runner.grade-test
  (:require [clojure.test :refer [deftest is testing]]
            [runner.grade :as grade]))

(deftest normalize-and-compare
  (testing "exact match"
    (is (:match? (grade/compare-outputs "a\nb" "a\nb"))))
  (testing "trailing whitespace"
    (is (:match? (grade/compare-outputs "a  \nb" "a\nb"))))
  (testing "crlf"
    (is (:match? (grade/compare-outputs "a\r\nb" "a\nb"))))
  (testing "trailing newlines"
    (is (:match? (grade/compare-outputs "a\nb\n\n" "a\nb"))))
  (testing "empty actual"
    (is (not (:match? (grade/compare-outputs "a" "")))))
  (testing "longer actual"
    (is (not (:match? (grade/compare-outputs "a" "a\nb"))))
    (is (= 2 (-> (grade/compare-outputs "a" "a\nb")
                 grade/first-diff-line
                 :line)))))

(deftest diff-cap
  (let [cmp (grade/compare-outputs "1\n2\n3" "1\nX\n3")
        diff (grade/build-diff cmp 20)]
    (is (= 2 (:first-diff-line diff)))
    (is (= 3 (count (:rows diff))))))

(defn -main [& _]
  (clojure.test/run-tests 'runner.grade-test))
