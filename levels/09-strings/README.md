# Level 09 — Strings

## What you'll learn
- `clojure.string` helpers
- Immutability — strings are not changed in place
- Subs, replace, split, join

## Concepts

### subs
Slice-like substring.

```clojure
(println (subs "abcdefgh" 2 5))
;; cde
```


### split / join
Break apart and rejoin.

```clojure
(require '[clojure.string :as str])
(println (str/join "-" (str/split "a,b" #",")))
;; a-b
```


## Common mistakes
- Using JavaScript-only methods — use `clojure.string` instead.
- Forgetting that strings are seq-able character by character.

## Before you start
Type every example above into `playground/scratch.clj` and run it with Babashka. Change a number and predict what happens before you run it again.

## Exercises
Work through the numbered files in order. Save each file to check it with the watcher.
