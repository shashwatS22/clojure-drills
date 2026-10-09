# Level 15 — Namespaces and effects

## What you'll learn
- `require` and namespaces
- `try` / `catch` / `finally` and `ex-info`
- `future`, `promise`, `delay`
- Reading files with `slurp`

## Concepts

### require
Load code from another namespace.

```clojure
(require '[clojure.string :as str])
(println (str/upper-case "ada"))
;; ADA
```


### try / catch
Handle errors without crashing.

```clojure
(try (/ 1 0) (catch Exception _ (println "caught")))
;; caught
```


### slurp
Read a whole file.

```clojure
(println (slurp "levels/15-namespaces-effects/data/sample.txt"))
;; hello from a file
```


## Common mistakes
- Wrong namespace name in `require`.
- Blocking forever on a promise that is never delivered.

## Before you start
Type every example above into `playground/scratch.clj` and run it with Babashka. Change a number and predict what happens before you run it again.

## Exercises
Work through the numbered files in order. Save each file to check it with the watcher.
