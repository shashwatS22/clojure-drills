# Level 12 — Maps

## What you'll learn
- Keywords as keys
- `assoc`, `dissoc`, `merge`
- JSON with Cheshire
- Safe access with `get-in`

## Concepts

### Keyword keys
Keywords are the usual map keys.

```clojure
(let [user {:name "Ada"}]
  (println (:name user)))
;; Ada
```


### merge
Combine maps; right-hand values win.

```clojure
(println (:b (merge {:a 1 :b 2} {:b 3})))
;; 3
```


## Common mistakes
- Using string keys when the data uses keywords.
- Forgetting Cheshire generates JSON without extra spaces.

## Before you start
Type every example above into `playground/scratch.clj` and run it with Babashka. Change a number and predict what happens before you run it again.

## Exercises
Work through the numbered files in order. Save each file to check it with the watcher.
