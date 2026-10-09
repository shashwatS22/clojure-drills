# Level 04 — Loops for printing and accumulating

## What you'll learn
- `doseq` and `range` for counting loops
- `loop` / `recur` for sums and counters
- Building number results step by step

## Concepts

### doseq
Run side effects like printing.

```clojure
(doseq [i (range 1 4)]
  (println i))
;; 1
;; 2
;; 3
```


### loop / recur
Tail-recursive accumulation.

```clojure
(loop [i 1 sum 0]
  (if (> i 3)
    (println sum)
    (recur (inc i) (+ sum i))))
;; 6
```


## Common mistakes
- Using `recur` outside `loop`/`fn`.
- Infinite loops when the counter never moves toward the end condition.
- Using strings to count digits when the exercise forbids it.

## Before you start
Type every example above into `playground/scratch.clj` and run it with Babashka. Change a number and predict what happens before you run it again.

## Exercises
Work through the numbered files in order. Save each file to check it with the watcher.
