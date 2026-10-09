(ns runner.report
  (:require [clojure.string :as str]
            [runner.grade :as grade]
            [runner.progress :as progress]
            [runner.resolve :as resolve]))

(def ^:private esc "\u001b[")

(defn- c [code s]
  (str esc code "m" s esc "0m"))

(defn dim [s] (c "2" s))
(defn green [s] (c "32" s))
(defn red [s] (c "31" s))
(defn yellow [s] (c "33" s))
(defn bold [s] (c "1" s))

(defn clear-screen! [config]
  (when (:clear-screen config true)
    (print "\u001Bc")
    (.flush ^java.io.PrintStream System/out)))

(defn print-banner []
  (println (dim "Clojure drills — save a file in levels/ to check it."))
  (println))

(defn level-progress-line [level-name & {:keys [root]}]
  (let [exs (resolve/list-exercises-in-level level-name :root root)
        passed (progress/passed-ids :root root)
        done (count (filter #(contains? passed (resolve/exercise-id level-name %)) exs))
        total (count exs)
        num (resolve/level-number level-name)]
    (str "Level " (format "%02d" (or num 0)) " — " done "/" total " done")))

(defn trim-error
  [stderr]
  (let [lines (str/split-lines stderr)
        trimmed (take 8 lines)]
    (str/join "\n" trimmed)))

(defn print-result
  [result & {:keys [config root]}]
  (let [config (or config (progress/load-config root))
        root (or root (resolve/repo-root))]
    (clear-screen! config)
    (case (:status result)
      :pass
      (do
        (println (green "✓ PASS") (:id result) (dim (str "(" (:duration-ms result) "ms)")))
        (println (dim (level-progress-line (:level result) :root root)))
        (when-let [levels (resolve/list-levels root)]
          (when (resolve/level-complete? (:level result) (progress/passed-ids :root root) :root root)
            (println)
            (println (bold (green (str "Level complete: " (:level result)))))
            (when-let [n (resolve/level-number (:level result))]
              (when-let [next-level (some #(when (= (resolve/level-number %) (inc n)) %) levels)]
                (println (dim (str "Next: " next-level))))))))

      :fail
      (do
        (println (red "✗ FAIL") (:id result))
        (when-let [diff (:diff result)]
          (println)
          (println (dim "  line  expected          your output"))
          (println (dim "  ────  ────────────────  ────────────────"))
          (doseq [{:keys [line expected actual first-diff?]} (:rows diff)]
            (let [e (or expected "(nothing)")
                  a (or actual "(nothing)")
                  mark (if first-diff? (str " " (yellow "← first difference")) "")]
              (println (str "  " (format "%4d" line) "  "
                            (format "%-16s" (subs e 0 (min 16 (count e))))
                            "  "
                            (format "%-16s" (subs a 0 (min 16 (count a))))
                            mark))))
          (when (:truncated? diff)
            (println (dim (str "... " (:more diff) " more lines")))))
        (when-let [h (:hint result)]
          (println (dim (str "Hint: " h)))))

      :error
      (do
        (println (red "✗ ERROR") (:id result))
        (when (seq (:stderr result))
          (println (red (trim-error (:stderr result))))))

      :timeout
      (println (red "✗ FAIL") (:id result) "—" (yellow "Timed out — you may have an infinite loop."))

      :missing-expected
      (println (red "✗ ERROR") (:id result) "— missing .expected.txt or _test.clj")

      nil)))

(defn print-progression-block [unfinished-id]
  (println (yellow "Finish the previous level first."))
  (println (dim (str "Start here: " unfinished-id))))

(defn print-dashboard [data]
  (println (bold "Progress"))
  (println)
  (doseq [{:keys [name done total]} (:levels data)]
    (let [pct (if (zero? total) 0 (int (* 100 (/ done total))))
          bar (str (apply str (repeat (quot pct 5) "█"))
                   (apply str (repeat (- 20 (quot pct 5)) "·")))]
      (println (format "%-35s %s %3d%% (%d/%d)" name bar pct done total))))
  (println)
  (println (str "Total: " (:total-done data) "/" (:total-exercises data)))
  (let [stuck (sort-by (fn [[_ m]] (- (:attempts m))) >
                       (remove (fn [[_ m]] (= "pass" (:status m)))
                               (:exercises data)))]
    (when-let [[id m] (first stuck)]
      (when (and id (> (:attempts m) 1))
        (println (dim (str "Most attempts: " id " (" (:attempts m) ")")))))))

(defn print-level-summary [results]
  (println (bold "Level check"))
  (println)
  (doseq [{:keys [id status duration-ms]} results]
    (let [icon (case status :pass "✓" :fail "✗" :error "!" :timeout "⏱" "?")
          col (case status :pass green :fail red :error red :timeout yellow identity)]
      (println (col (str icon " " id)) (dim (str "(" duration-ms "ms)")))))
  (let [passed (count (filter #(= :pass (:status %)) results))
        total (count results)]
    (println)
    (println (str passed "/" total " passed"))))
