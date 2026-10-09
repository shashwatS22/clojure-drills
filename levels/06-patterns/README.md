# Level 06 — Patterns

## What you'll learn
- Nested loops for rows and columns
- Building one row string, then one `println` per row
- Padding with `format`

## Concepts

### One println per row
Build the full row first.

```clojure
(let [row (apply str (repeat 5 "*"))]
  (println row))
;; *****
```


### format padding
Pad numbers to a fixed width.

```clojure
(println (format "%4d" 7))
;;    7
```


## Common mistakes
- Many `print` calls per row — build one string instead.
- Off-by-one row counts.
- Extra spaces at row ends.

## Before you start
Type every example above into `playground/scratch.clj` and run it with Babashka. Change a number and predict what happens before you run it again.

## Exercises
Work through the numbered files in order. Save each file to check it with the watcher.
