# Level 10 — Vectors

## What you'll learn
- Immutable vectors with `conj`, `pop`, `peek`
- Indexing, subvec, and loops
- Classic array-style drills without mutation

## Concepts

### conj
Adds at the end, returns a new vector.

```clojure
(println (conj [1 2] 3))
;; [1 2 3]
```


### peek / pop
Look at or remove the last element.

```clojure
(println (peek [1 2 3]))
(println (pop [1 2 3]))
;; 3
;; [1 2]
```


## Common mistakes
- Expecting `conj` to mutate the original vector.
- Using `first` when you meant the last element — use `peek` or `last`.

## Before you start
Type every example above into `playground/scratch.clj` and run it with Babashka. Change a number and predict what happens before you run it again.

## Exercises
Work through the numbered files in order. Save each file to check it with the watcher.
