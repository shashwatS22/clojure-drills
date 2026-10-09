# Level 11 — Sequence transforms

## What you'll learn
- `map`, `filter`, `reduce`
- `sort` and `sort-by`
- Threading with `->>`
- One-level vs full flatten

## Concepts

### map / filter
Transform or keep elements.

```clojure
(println (map inc [1 2 3]))
;; (2 3 4)
```


### ->>
Thread a collection through steps.

```clojure
(->> [1 2 3 4] (filter even?) (map #(* % %)) (reduce +))
;; 20
```


## Common mistakes
- Using `flatten` when you only need one level.
- Sorting numbers as strings — use `sort` on numbers directly.

## Before you start
Type every example above into `playground/scratch.clj` and run it with Babashka. Change a number and predict what happens before you run it again.

## Exercises
Work through the numbered files in order. Save each file to check it with the watcher.
