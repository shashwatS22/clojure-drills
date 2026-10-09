#!/usr/bin/env bb

(load-file (first *command-line-args*))
(load-file (second *command-line-args*))
(require '[clojure.test :as t])
(let [result (t/run-all-tests)]
  (when (pos? (+ (:error result) (:fail result)))
    (System/exit 1)))
