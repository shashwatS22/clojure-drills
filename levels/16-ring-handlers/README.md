# Level 16 — Ring handlers

## What you'll learn
- Ring request and response maps
- `ring.util.response` helpers
- Reading `:request-method`, `:uri`, and headers
- Manual routing before Compojure
- JSON bodies with Cheshire

## Concepts

### Response map
A Ring handler returns a map with `:status`, `:headers`, and `:body`.

```clojure
(println (:body {:status 200 :headers {} :body "ok"}))
;; ok
```

### ring.util.response
Helpers build the same map for you.

```clojure
(require '[ring.util.response :refer [response]])
(println (:body (response "hello")))
;; hello
```

## Common mistakes
- Header keys in requests are lower-case strings (`"authorization"`), not keywords.
- Forgetting `:body` must be a string for typical HTTP responses.
- Using `not-found` without a request map in Ring 1.11 — use `(not-found {})`.

## Before you start
Type every example above into `playground/scratch.clj` and run with Babashka from the repo root.

## Exercises
Work through the numbered files in order. Save each file to check it with the watcher.
