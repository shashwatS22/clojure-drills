# Level 02 — Operators

## What you'll learn
- Arithmetic and ratios like `17/5`
- Integer division with `quot` and remainders with `rem`/`mod`
- Logic with `and`, `or`, `not`
- Comparisons with `=`
- Parsing numbers from strings

## Concepts

### Division
`(/ 17 5)` keeps an exact ratio.

```clojure
(println (/ 17 5))
;; 17/5
```


### rem vs mod
Remainders differ for negative numbers.

```clojure
(println (rem -7 3))
(println (mod -7 3))
;; -1
;; 2
```


### inc
Use `(inc x)` instead of `x++`.

```clojure
(let [x 5]
  (println (inc x)))
;; 6
```


## Common mistakes
- Using `/` when you wanted whole-number division — use `quot`.
- Confusing `rem` and `mod` on negative numbers.
- Concatenating strings with `+` — use `str` instead.

## Before you start
Type every example above into `playground/scratch.clj` and run it with Babashka. Change a number and predict what happens before you run it again.

## Exercises
Work through the numbered files in order. Save each file to check it with the watcher.
