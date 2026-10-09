# Level 08 — Functions

## What you'll learn
- `defn`, anonymous `#()` fns, multi-arity
- Variadic args with `&`
- `apply` and higher-order functions
- Atoms for mutable counter state
- `prn` to show return vs side-effect printing

## Concepts

### defn
Named function with parameters.

```clojure
(defn add [a b] (+ a b))
(println (add 2 3))
;; 5
```


### apply
Call a function with a collection of args.

```clojure
(println (apply max [4 9 2]))
;; 9
```


### atom counter
Swap an atom for increasing state.

```clojure
(let [n (atom 0)] (swap! n inc) (println @n))
;; 1
```


## Common mistakes
- Confusing `println` (side effect) with the return value — use `prn` to inspect.
- Forgetting base case in higher-order helpers.

## Before you start
Type every example above into `playground/scratch.clj` and run it with Babashka. Change a number and predict what happens before you run it again.

## Exercises
Work through the numbered files in order. Save each file to check it with the watcher.
