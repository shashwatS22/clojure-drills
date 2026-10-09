# Level 01 — Print and variables

## What you'll learn
- Printing lines with `println`
- Binding names with `def` and `let`
- Shadowing values without reassignment
- Checking types with `number?`, `string?`, and friends
- Building strings and simple output

## Concepts

### println
Prints a line and adds a newline.

```clojure
(println "Hello")
;; Hello
```


### let shadowing
Use a new `let` to bind the same name to a new value.

```clojure
(let [count 10]
  (println count)
  (let [count 20]
    (println count)))
;; 10
;; 20
```


### Type predicates
Clojure uses predicates instead of JavaScript `typeof`.

```clojure
(println (number? 5))
(println (string? "hi"))
;; true
;; true
```


## Common mistakes
- Trying to reassign a `let` binding — use another `let` instead.
- Forgetting quotes around strings.
- Using `print` when you need a full line (`println`).

## Before you start
Type every example above into `playground/scratch.clj` and run it with Babashka. Change a number and predict what happens before you run it again.

## Exercises
Work through the numbered files in order. Save each file to check it with the watcher.
