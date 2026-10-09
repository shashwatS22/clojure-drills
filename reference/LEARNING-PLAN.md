# Zero to Clojure HTTP — A Full-Time Learning Plan

**Audience:** a beginner who can already write `println`, a `for` loop, and an `if`, but nothing beyond that.
**Commitment:** 3+ hours/day, ~5–6 days a week.
**End state:** solid Clojure fundamentals, then a small HTTP API on **Ring**, **Compojure**, and **Jetty**, with algorithm practice on Exercism (or LeetCode if you stay on the original JS track).

There are two documents:

| File | Who it's for |
|---|---|
| `LEARNING-PLAN.md` (this file) | You and her — the roadmap, the routine, what to learn when |
| `CURSOR-BUILD-SPEC.md` | Hand this to Cursor — it builds the practice repo, all 228 exercises (190 language + 38 HTTP), and the auto-grader |

---

## 1. The core idea

She gets one repo (`js-bootcamp`) running locally. It's a Node project with a file watcher. She opens an exercise file, writes code, hits save, and the terminal immediately tells her **PASS** or **FAIL** with a line-by-line diff against the expected output.

That's the whole loop. No setup friction, no "did I run it right", no waiting for feedback. Save → verdict → fix → save.

**Two parallel tracks run every day:**

- **Track A — Drills (the repo).** 190 auto-graded exercises across 15 levels. This is where she learns the *language*.
- **Track B — DSA (LeetCode).** Problems from Striver's A2Z sheet, solved on LeetCode in JavaScript. This is where she learns to *think*.

Track A always stays ahead of Track B. She never gets a LeetCode problem that needs syntax she hasn't drilled.

---

## 2. Daily routine (3.5 hours)

| Block | Time | What |
|---|---|---|
| 1. Concept | 30 min | Read the level's `README.md` in the repo, type out the examples in `playground/scratch.js`. Typing, not copy-pasting. |
| 2. Drills | 90 min | Work through that level's exercises until they're green. |
| 3. DSA | 60 min | 2–4 LeetCode problems from the current Striver section. |
| 4. Review | 20 min | Re-solve one problem from 2 days ago **from a blank file**. Then write 3 lines in `NOTES.md` about what tripped her up. |

The review block is the one people skip and it's the one that makes it stick. Don't skip it.

### Rules that matter

1. **No copy-paste into exercise files.** Type everything.
2. **15-minute rule.** Stuck for 15 min on a drill → read the level README again. Still stuck at 25 min → `npm run solution <id>`, read it, close it, delete her attempt, and rewrite it from memory.
3. **Never move to the next level until the current one is 100% green.** The runner enforces this by default (`strictProgression: true` in config).
4. **LeetCode uses JavaScript**, not any other language. Consistency beats variety at this stage.
5. **One "concept debt" list.** Anything she doesn't understand goes into `NOTES.md` under `## Confused about`. You review that list with her every few days. This is your main job as the teacher.

---

## 3. Phase overview

| Phase | Weeks | What | Deliverable |
|---|---|---|---|
| **1. JavaScript** | 1–4 | 15 levels, 190 drills. Variables → recursion → hashing → async. | All levels green |
| **2. DSA foundation** | 1–6 (parallel) | Striver Step 1 & 2 on LeetCode | ~60 problems solved |
| **3. Ring handlers** | 5–6 | Request/response maps, `ring.util.response`, manual routing, JSON bodies | Level `16-ring-handlers` green |
| **4. Compojure** | 6–7 | `GET`/`POST`, path and query params, combining routes | Level `17-compojure` green |
| **5. Middleware** | 7–8 | Handler wrappers, auth header, JSON middleware, ordering | Level `18-middleware` green |
| **6. Jetty** | 8–9 | `run-jetty`, HTTP client, in-process API capstone | Level `19-jetty` green + notes API |

**Why this order:** Ring handlers are pure functions — no server until level 19. Compojure is sugar on top of the same model. Middleware is easier once routing is automatic. Jetty ties it together with real TCP, still graded via stdout from a short-lived process.

---

## 4. Phase 1 in detail — the 15 levels

Each level in the repo has a `README.md` you write once (Cursor drafts it) covering the concept, then the exercises. Here's what each level teaches and what it unlocks.

| # | Level | Drills | Concepts taught | Unlocks on LeetCode |
|---|---|---|---|---|
| 01 | Print & Variables | 12 | `console.log`, `let`/`const`, types, template literals, `typeof` | — |
| 02 | Operators | 12 | arithmetic, `%`, `==` vs `===`, logical ops, ternary, `Math.*` | — |
| 03 | Conditionals | 12 | `if`/`else if`/`else`, `switch`, truthy/falsy | Striver Lec 1 basics |
| 04 | For loops | 14 | `for`, accumulators, `break`/`continue`, loop-based number work | FizzBuzz, simple sums |
| 05 | While loops | 10 | `while`, `do...while`, digit extraction via `%` and `/` | — |
| 06 | Nested loops & patterns | 16 | loops inside loops, row/column thinking | Striver Lec 2 (22 patterns) |
| 07 | Number problems | 14 | primes, divisors, GCD, Armstrong, palindrome numbers | **Striver Lec 4 — Basic Maths** |
| 08 | Functions | 14 | declarations, arrows, params, return, scope, closures, callbacks | Refactoring all prior work |
| 09 | Strings | 14 | indexing, immutability, all core string methods | Striver Strings (basic) |
| 10 | Arrays | 16 | indexing, mutation methods, traversal, search, rotation | **Striver Step 3 — Arrays (easy)** |
| 11 | Array HOFs | 12 | `map`, `filter`, `reduce`, `find`, `sort`, `some`/`every` | Cleaner LeetCode solutions |
| 12 | Objects & JSON | 12 | key access, nesting, destructuring, spread, `JSON.*` | Data-shaped problems |
| 13 | Recursion | 10 | base case, recursive case, call stack | **Striver Lec 5 — Recursion** |
| 14 | Hashing | 10 | `Map`, `Set`, frequency counting, `O(1)` lookup | **Striver Lec 6 — Hashing**, Two Sum |
| 15 | Modules, errors, async | 12 | `import`/`export`, `try`/`catch`, Promises, `async`/`await`, `fs` | Required for React/Next.js |

**Total: 190 exercises.**

The full exercise list — every file name, task, fixed inputs, and expected output — is in `CURSOR-BUILD-SPEC.md` § 8.

### Suggested pacing (full-time)

| Days | Levels |
|---|---|
| 1–2 | 01, 02 |
| 3–4 | 03, 04 |
| 5–6 | 05, 06 |
| 7–8 | 07 |
| 9–10 | 08 |
| 11–12 | 09 |
| 13–15 | 10, 11 |
| 16–17 | 12 |
| 18–19 | 13 |
| 20–21 | 14 |
| 22–24 | 15 + full review |

Level 06 (patterns) and level 13 (recursion) are the two walls. Expect her to slow down there. That's normal — patterns build spatial loop reasoning and recursion breaks people's mental model. Budget extra time, don't rush them.

---

## 5. Track B — the Striver A2Z mapping

Source: <https://takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z>

She reads the problem on the Striver sheet, then solves it **on LeetCode in JavaScript**. Striver's videos are in C++/Java — that's fine, the logic transfers. Only the syntax differs, and by then she'll know the syntax.

| Order | Striver section | Start after repo level | Approx. problems |
|---|---|---|---|
| 1 | Step 1, Lec 1 — Language basics | 03 | Covered by drills |
| 2 | Step 1, Lec 2 — Patterns (22) | 06 | 22 |
| 3 | Step 1, Lec 4 — Basic Maths | 07 | 7 |
| 4 | Step 1, Lec 5 — Basic Recursion | 13 | 9 |
| 5 | Step 1, Lec 6 — Basic Hashing | 14 | 3 |
| 6 | Step 2 — Sorting techniques | 13 | 7 |
| 7 | Step 3 — Arrays (Easy) | 10 | ~14 |
| 8 | Step 3 — Arrays (Medium) | 14 | ~14 |
| 9 | Step 4 — Binary Search (1D) | after Phase 1 | ~13 |
| 10 | Step 5 — Strings (Basic) | 09 | ~7 |

**Target by end of Phase 1: ~60 problems.** Steps 2 and 3 are the first real algorithmic work — she can still be on those when Phase 3 (Ring) begins. DSA continues in the background; it does not need to finish before HTTP drills start.

### LeetCode discipline

- Time-box every problem to 30 minutes. Then look at the editorial, understand it, close it, and write it from scratch.
- After solving, write the approach in one plain-English sentence in `NOTES.md`. If she can't, she didn't solve it — she guessed.
- Re-solve any problem she needed help with, 3 days later.

---

## 6. Phase 3 — Ring handlers (`16-ring-handlers`, 12 drills)

Same PASS/FAIL loop as Phase 1. Each file defines a handler (or uses helpers) and prints `:status`, `:body`, or selected fields — no network yet.

**Topics, in order:**

1. A response map: `:status`, `:headers`, `:body`
2. `ring.util.response`: `response`, `status`, `content-type`, `header`
3. `not-found`, `redirect`
4. Reading `:request-method`, `:uri`, `:headers` from a GIVEN request map
5. Branching on method + path without a router library
6. JSON response bodies with Cheshire + `application/json`

**Duration:** ~4–5 days full-time.

---

## 7. Phase 4 — Compojure (`17-compojure`, 10 drills)

Compojure turns route definitions into one Ring handler.

**Topics:**

1. `GET` / `POST` routes, static paths
2. Path params (`:id`)
3. Query params (`wrap-params`, `wrap-keyword-params`)
4. `context`, catch-all / not-found route
5. Combining route tables; one JSON “item by id” route

**Duration:** ~3–4 days full-time.

---

## 8. Phase 5 — Middleware (`18-middleware`, 8 drills)

A middleware is `(fn [handler] (fn [request] ...))`.

**Topics:**

1. Adding response headers in middleware
2. Simple token check → 401
3. `ring.middleware.json-params` / JSON response helpers
4. Order of middleware — inner vs outer behavior

**Duration:** ~2–3 days full-time.

---

## 9. Phase 6 — Jetty (`19-jetty`, 8 drills)

**Topics:**

1. `ring.adapter.jetty/run-jetty` with `:join? false`, port `0`
2. `babashka.http-client` against `localhost`
3. Stop the server before exit so the grader finishes
4. Capstone: in-memory notes API — fixed transcript printed to stdout

**Duration:** ~3–4 days full-time.

**After the repo:** deploy a small Ring app (Docker, Railway, or a VPS), add a database (next step outside this drill repo).

---

## 10. Milestones — how to know she's ready to move on

| Gate | Test |
|---|---|
| Leave Phase 1 | All 190 drills green. Can write "count vowels in a string" and "second largest distinct number in a vector" from a blank file in under 5 minutes each. |
| Leave Phase 3 | Can explain request vs response map keys and write a handler that returns 404 for unknown paths without Compojure. |
| Leave Phase 5 | Can add auth middleware and explain why order matters. |
| Done (Phase 6) | Level 19 green; can sketch a Compojure + Jetty app from memory and explain where routing, middleware, and the adapter sit. |

---

## 11. Your job in this

The repo handles correctness. It cannot handle the things that actually cause beginners to quit.

- **Review `NOTES.md` every 2–3 days.** The "Confused about" list is your teaching agenda.
- **Explain *why*, not *how*.** When she asks about `===`, don't give the rule — show her a bug it causes.
- **Let her struggle for 15 minutes.** Rescuing too early is the most common way well-meaning teachers slow someone down.
- **Celebrate green levels.** 190 exercises is a long grind; visible progress is what carries people through week 3.
- **Don't add topics ahead of schedule** because they seem interesting. The ordering here is deliberate — every level only needs things from earlier levels.
