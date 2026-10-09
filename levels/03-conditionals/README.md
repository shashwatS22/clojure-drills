# Level 03 — Conditionals

## What you'll learn
- `if` for two-way choices
- `cond` for many conditions
- `case` for matching one value
- Truthy values — only `nil` and `false` are false

## Concepts

### if
Pick one branch.

```clojure
(if (> 3 1) (println "yes") (println "no"))
;; yes
```


### cond
Like a chain of else-if.

```clojure
(def n -14)
(cond
  (> n 0) (println "positive")
  (< n 0) (println "negative")
  :else (println "zero"))
;; negative
```


### case
Match a single value.

```clojure
(def day 2)
(println (case day 1 "Mon" 2 "Tue" "other"))
;; Tue
```


## Common mistakes
- Treating `0` or `""` as false — in Clojure they are truthy.
- Forgetting the `:else` branch in `cond`.
- Using `case` without a default for unknown values.

## Before you start
Type every example above into `playground/scratch.clj` and run it with Babashka. Change a number and predict what happens before you run it again.

## Exercises
Work through the numbered files in order. Save each file to check it with the watcher.
