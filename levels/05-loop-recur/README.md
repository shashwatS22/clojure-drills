# Level 05 — loop/recur drills

## What you'll learn
- Digit extraction with `quot` and `rem`
- Classic while-style algorithms with `loop`/`recur`
- A do-while style drill that always runs once

## Concepts

### Digit sum
Peel off the last digit until the number is zero.

```clojure
(loop [n 482 sum 0]
  (if (zero? n)
    (println sum)
    (recur (quot n 10) (+ sum (rem n 10)))))
;; 14
```


### Run once
Print before checking, like do-while.

```clojure
(println "ran once")
(loop [once true]
  (when once
    (println "loop finished")
    (recur false)))
;; ran once
;; loop finished
```


## Common mistakes
- Forgetting to shrink `n` in digit loops.
- Using `/` on integers when you mean `quot`.

## Before you start
Type every example above into `playground/scratch.clj` and run it with Babashka. Change a number and predict what happens before you run it again.

## Exercises
Work through the numbered files in order. Save each file to check it with the watcher.
