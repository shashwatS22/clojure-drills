# Level 18 — Middleware

## What you'll learn
- Middleware as `(fn [handler] (fn [request] ...))`
- Adding response headers
- Simple auth checks
- JSON parse/generate in middleware
- Order of middleware in the stack

## Concepts

### A tiny middleware
The outer function receives the inner handler.

```clojure
(defn wrap-ok [handler]
  (fn [req]
    (assoc (handler req) :body "ok")))
(defn app [_] {:status 200 :headers {} :body ""})
(println (:body ((wrap-ok app) {})))
;; ok
```

### Stack order
`((wrap-b (wrap-a handler))` — request passes through `b` then `a` then `handler`; the response unwinds the opposite way.

## Common mistakes
- Threading `->` into middleware factories incorrectly — `(wrap-a (wrap-b handler))` not `(-> handler wrap-a wrap-b)` unless `wrap-a` is a unary function.
- Checking the wrong header name (use `"x-token"` not `:x-token` in `:headers`).

## Before you start
Re-read level 16 if response maps feel rusty.

## Exercises
Work through the numbered files in order.
