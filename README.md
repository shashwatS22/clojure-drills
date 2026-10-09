# Clojure drills

Auto-graded Clojure practice: open an exercise under `levels/`, write code, save, and the terminal shows **PASS** or **FAIL** with a line diff.

## Requirements

- [Babashka](https://github.com/babashka/babashka) 1.4+ (`bb --version`)

On macOS with Homebrew:

```bash
brew install borkdude/brew/babashka
```

## Quick start

```bash
cd clojure-drills
bb dev
```

Leave that terminal open. In your editor, open any file in `levels/` (for example `levels/01-print-and-variables/01-hello.clj`), write your code below the comment, and **save**. The watcher grades that file immediately.

Other commands:

| Command | Purpose |
|---------|---------|
| `bb check 01-print-and-variables/01-hello` | Grade one exercise once |
| `bb check-level 01 --solutions` | Grade every exercise in level 01 (maintainers) |
| `bb progress` | Progress dashboard |
| `bb solution <id> --force` | Show reference solution (locked until 3 failures by default) |
| `bb reset <id> --yes` | Restore the stub and clear progress for one exercise |
| `bb test` | Run the runner’s unit tests |

## What PASS and FAIL look like

**PASS** (screen clears, then):

```
✓ PASS 01-print-and-variables/01-hello (18ms)
Level 01 — 1/12 done
```

**FAIL**:

```
✗ FAIL 04-for-loops/12-fibonacci

  line  expected          your output
  ────  ────────────────  ────────────────
   4    2                 3      ← first difference
```

## Rules that matter

1. **Type, don’t paste** into exercise files.
2. **15-minute rule:** stuck 15 minutes → re-read the level `README.md`. Still stuck at 25 → `bb solution <id> --force`, read it, close it, delete your attempt, rewrite from memory.
3. **Finish a level completely** before relying on the next (`strictProgression` in `config.edn`).
4. Scratch space: `playground/scratch.clj` — run with `bb playground/scratch.clj` from the repo root.
5. Notes: edit `NOTES.md` (especially **Confused about**).

## Layout

- `levels/` — your exercises (15 levels, 190 drills)
- `stubs/` — pristine copies used by `bb reset`
- `.solutions/` — reference solutions (for `bb solution` and generating expected output)
- `runner/` — watcher and grader (Babashka)
- `reference/` — original JavaScript bootcamp spec (for authors)

See [LEARNING-PLAN.md](LEARNING-PLAN.md) for pacing and how this pairs with algorithm practice.
