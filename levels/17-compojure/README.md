# Level 17 — Compojure

## What you'll learn
- `defroutes` and `routes`
- `GET`, `POST`, path params, query params
- `context` for path prefixes
- Combining route tables

## Concepts

### Route as a handler
Compojure turns route definitions into one Ring handler function.

```clojure
(def req {:request-method :get :uri "/ping" :headers {}})
(println (:uri req))
;; /ping
```

You will use `compojure.core` in these exercises. The grader runs them with the **Clojure CLI** (`clojure -M:run-exercise`) because Compojure does not load under Babashka.

### Query params
Wrap the app with `wrap-params` so `:params` is populated from the query string.

```clojure
(require '[ring.middleware.params :refer [params-request]])
(println (get (params-request {:query-string "q=clojure"}) :params))
;; {"q" "clojure"}
```

## Common mistakes
- Forgetting `wrap-params` before reading query parameters.
- Using keyword params without `wrap-keyword-params`.
- Expecting POST to work on a route that only defines GET.

## Before you start
Ensure `clojure` is on your PATH. Exercises still use the same save-to-grade workflow; the runner picks Clojure automatically for this level.

## Exercises
Work through the numbered files in order.
