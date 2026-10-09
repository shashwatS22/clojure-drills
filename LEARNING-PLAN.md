# Clojure drills — learning plan

**Audience:** you can already run a program and write a simple `if`, but Clojure still feels new.  
**Commitment:** 3+ hours/day, about 5–6 days a week.  
**End state:** solid Clojure fundamentals, then a small HTTP API on **Ring**, **Compojure**, and **Jetty**, plus a parallel algorithm habit on [Exercism Clojure](https://exercism.org/tracks/clojure).

## The loop

One repo (`clojure-drills`), Babashka, and a file watcher. Open an exercise, write code, save → **PASS** or **FAIL** with a diff.

**Two tracks:**

| Track | What | Where |
|-------|------|--------|
| **A — Drills** | Language + HTTP, 228 exercises, 19 levels | This repo (`bb dev`) |
| **B — Algorithms** | Problem solving | Exercism Clojure (after the matching level) |

Keep Track A ahead of Track B so you are never solving problems that need syntax you have not drilled.

## Daily routine (~3.5 hours)

| Block | Time | Activity |
|-------|------|----------|
| Concept | 30 min | Read the level `README.md`; type examples in `playground/scratch.clj` |
| Drills | 90 min | Exercises until green |
| Algorithms | 60 min | 2–4 Exercism exercises from the current section |
| Review | 20 min | Re-solve one drill from two days ago in a blank file; update `NOTES.md` |

## Phase 1 — language (levels 01–15)

| # | Folder | Focus |
|---|--------|--------|
| 01 | `01-print-and-variables` | `println`, `let`, types, `str`, predicates |
| 02 | `02-operators` | math, `quot`/`rem`/`mod`, `=`, `==` |
| 03 | `03-conditionals` | `if`, `cond`, `case`, truthiness |
| 04 | `04-for-loops` | `doseq`, `range`, `loop`/`recur` |
| 05 | `05-loop-recur` | digit tricks, GCD, binary, Collatz |
| 06 | `06-patterns` | nested loops, string rows |
| 07 | `07-number-problems` | primes, divisors, GCD, LCM |
| 08 | `08-functions` | `defn`, `#()`, higher-order fns, `atom` |
| 09 | `09-strings` | `clojure.string`, characters |
| 10 | `10-vectors` | immutable vector ops |
| 11 | `11-seq-transforms` | `map`, `filter`, `reduce`, `->>` |
| 12 | `12-maps` | keywords, `merge`, JSON (Cheshire) |
| 13 | `13-recursion` | base case, `recur` |
| 14 | `14-frequency` | maps for counting, `clojure.set` |
| 15 | `15-namespaces-effects` | `load-file`, errors, futures, `slurp` |

**Pacing (full-time):** about 3–4 weeks for these 190 drills. Levels **06** (patterns) and **13** (recursion) usually take longer — budget extra days.

## Phase 2 — HTTP backend (levels 16–19)

| # | Folder | Focus |
|---|--------|--------|
| 16 | `16-ring-handlers` | request/response maps, `ring.util.response`, manual routing, JSON |
| 17 | `17-compojure` | routes, path/query params (**Clojure CLI** grader) |
| 18 | `18-middleware` | handler wrappers, auth, JSON middleware, order |
| 19 | `19-jetty` | `run-jetty`, Hato client, notes API capstone (**Clojure CLI**) |

**Pacing:** about 2 weeks full-time after phase 1. Level **19** is slower (real server startup).

Install [Clojure CLI](https://clojure.org/guides/install_clojure) before level 17. Levels 16 and 18 still grade with Babashka from the repo root.

## Exercism mapping (Track B)

| Start after level | Exercism area |
|-------------------|---------------|
| 03 | Easy exercises using `if` / `cond` |
| 06 | Loop and string layout problems |
| 07 | Number theory style |
| 10 | List / vector exercises |
| 13 | Recursion track exercises |
| 14 | Problems needing frequency maps |

Use Exercism’s editor in Clojure; submit and read community solutions after your own attempt.

## Milestones

**Phase 1 done**

- All **190** language drills green.
- From a blank file in under 5 minutes each: **count vowels in a string** and **second largest distinct number in a vector**, without looking at old code.

**Phase 2 done**

- All **38** HTTP drills green (**228** total).
- Can sketch a Compojure app on Jetty and explain where routing, middleware, and the adapter sit.

## Teaching notes (if someone is pairing with you)

- Review `NOTES.md` every few days — **Confused about** is the agenda.
- Explain **why** (e.g. why only `nil`/`false` are false), not only the rule.
- Let the learner sit with a FAIL for 15 minutes before hinting.
- Celebrate finished levels — 228 exercises is a long grind.

## Author tooling

- Regenerate expected output: `bb gen-expected` (after editing `.solutions/`).
- Regenerate stubs from Python: `python3 tools/generate_content.py`.
- Full solution check: `bb check-level NN --solutions` for `NN` = `01` … `19`.
- Regenerate HTTP track content: `python3 tools/scaffold_http_levels.py` (maintainers).
