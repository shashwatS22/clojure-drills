# Level 14 — Frequency and sets

## What you'll learn
- `frequencies`, `update`, `fnil`
- `clojure.set` union and intersection
- Counting for anagram and two-sum style problems

## Concepts

### frequencies
Count occurrences in one pass.

```clojure
(println (frequencies "banana"))
;; {\a 3, \b 1, \n 2}
```


### set ops
Union and intersection.

```clojure
(require '[clojure.set :as set])
(println (set/union #{1 2} #{2 3}))
;; #{1 2 3}
```


## Common mistakes
- Losing insertion order when printing counts — follow the exercise pattern.
- Building frequency maps by hand when `frequencies` fits.

## Before you start
Type every example above into `playground/scratch.clj` and run it with Babashka. Change a number and predict what happens before you run it again.

## Exercises
Work through the numbered files in order. Save each file to check it with the watcher.
