(ns runner.grade
  (:require [clojure.string :as str]))

(defn normalize
  "Normalize stdout for comparison (line endings, trailing space, trailing blanks)."
  [s]
  (-> s
      (str/replace #"\r\n" "\n")
      str/split-lines
      (->> (map #(str/replace % #"\s+$" ""))
           (str/join "\n"))
      (str/replace #"\n+$" "")))

(defn lines [s]
  (if (str/blank? s) [] (str/split-lines s)))

(defn compare-outputs
  [expected actual]
  (let [exp-n (normalize expected)
        act-n (normalize actual)]
    (if (= exp-n act-n)
      {:match? true}
      {:match? false
       :expected-lines (lines exp-n)
       :actual-lines (lines act-n)})))

(defn first-diff-line
  [{:keys [expected-lines actual-lines]}]
  (let [max-i (max (count expected-lines) (count actual-lines))]
    (first
     (for [i (range max-i)
           :let [e (nth expected-lines i nil)
                 a (nth actual-lines i nil)]
           :when (not= e a)]
       {:line (inc i) :expected e :actual a}))))

(defn build-diff
  "Up to max-lines rows for the two-column diff table."
  [comparison max-lines]
  (when-not (:match? comparison)
    (let [exp (:expected-lines comparison)
          act (:actual-lines comparison)
          max-i (max (count exp) (count act))
          diff-at (some-> (first-diff-line comparison) :line)
          rows (for [i (range (min max-i max-lines))
                     :let [e (nth exp i nil)
                           a (nth act i nil)]]
                 {:line (inc i)
                  :expected e
                  :actual a
                  :first-diff? (= (inc i) diff-at)})]
      {:rows rows
       :truncated? (> max-i max-lines)
       :more (- max-i max-lines)
       :first-diff-line diff-at})))
