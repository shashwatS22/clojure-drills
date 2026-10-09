# Level 19 — Jetty

## What you'll learn
- `ring.adapter.jetty/run-jetty` with `:port 0` and `:join? false`
- HTTP requests against a live server with Hato
- Stopping the server so the process exits
- A small in-memory HTTP API

## Concepts

### Why port 0?
The OS assigns a free port. Read it from the server object — do not print the port in exercise output.

```clojure
(println (pos? 8080))
;; true
```

Exercises use `run-jetty` and `hato.client` over `http://127.0.0.1`. The grader runs this level with the **Clojure CLI** and allows a longer timeout (30s) for JVM + Jetty startup.

### Lifecycle
Start Jetty, call the app over HTTP, print the required lines, then `(.stop server)`.

## Common mistakes
- `:join? true` blocks forever — use `:join? false`.
- POST bodies from Jetty may be an `InputStream` — slurp or use a `body-string` helper.
- Hato throws on 4xx by default — use `:throw-exceptions false` when you need the status code.

## Before you start
Finish levels 16–18. Have `clojure` installed alongside Babashka.

## Exercises
Work through the numbered files in order.
