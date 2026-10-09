# Level 13 — Recursion

## What you'll learn
- Base case and recursive case
- Using `recur` for tail recursion
- Thinking in return values (tests on later exercises)

## Concepts

### factorial stack
Each call waits for the next.

```clojure
;; (factorial 4)
;; → (* 4 (factorial 3))
;; → (* 4 (* 3 (factorial 2)))
;; → … until factorial 1 → 1
```


### sum-to
Classic downward recursion.

```clojure
(defn sum-to [n]
  (if (<= n 1) n (+ n (sum-to (dec n)))))
(println (sum-to 5))
;; 15
```


## Common mistakes
- Missing base case → stack overflow.
- Using loops when the exercise asks for recursion.

## Before you start
Type every example above into `playground/scratch.clj` and run it with Babashka. Change a number and predict what happens before you run it again.

## Exercises
Work through the numbered files in order. Save each file to check it with the watcher.
