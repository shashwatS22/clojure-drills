#!/usr/bin/env python3
"""
Generate all Clojure drills practice content (190 exercises).
Run from repo root: python3 tools/generate_content.py

Implementation is split across this file plus generate_content_bank.py and
generate_content_readmes.py in the same directory (loaded via importlib).
"""

from __future__ import annotations

import importlib.util
import sys
import textwrap
from pathlib import Path
from typing import Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
TOOLS_DIR = Path(__file__).resolve().parent

LEVEL_FOLDERS = [
    ("01-print-and-variables", 12),
    ("02-operators", 12),
    ("03-conditionals", 12),
    ("04-for-loops", 14),
    ("05-loop-recur", 10),
    ("06-patterns", 16),
    ("07-number-problems", 14),
    ("08-functions", 14),
    ("09-strings", 14),
    ("10-vectors", 16),
    ("11-seq-transforms", 12),
    ("12-maps", 12),
    ("13-recursion", 10),
    ("14-frequency", 10),
    ("15-namespaces-effects", 12),
]

TEST_GRADED = {
    "08-functions": {
        "01-add",
        "02-arrow-multiply",
        "03-default-params",
        "04-is-even",
        "05-min-max-object",
        "06-rest-sum",
        "07-apply-twice",
        "08-make-multiplier",
    },
    "13-recursion": {
        "04-sum-to-n",
        "05-factorial",
        "06-reverse-array",
        "07-is-palindrome",
        "08-fibonacci",
        "09-power",
        "10-sum-digits",
    },
}


def _load_module(name: str):
    path = TOOLS_DIR / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"Cannot load module {name} from {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def make_stub(ex) -> str:
    lines = [
        f";; {ex.level} / {ex.basename}",
        ";;",
        ";; TASK",
        *[f";; {line}" for line in textwrap.wrap(ex.task, width=70)],
        ";;",
    ]
    if ex.hint.strip():
        lines += [";; HINT", *[f";; {line}" for line in textwrap.wrap(ex.hint, width=70)], ";;"]
    if ex.given.strip():
        lines += [";; DO NOT CHANGE the GIVEN values.", ";;"]
    lines += [";; EXPECTED OUTPUT"]
    for eline in ex.expected.split("\n"):
        lines.append(f";; {eline}")
    lines.append(";;")
    if ex.given.strip():
        lines.append(";; ---- GIVEN ----")
        lines.extend(ex.given.splitlines())
        lines.append(";; ---------------")
        lines.append(";;")
    if ex.fn_stub:
        name, args, default = ex.fn_stub
        lines.append(f";; Export: (defn {name} {args} ...)")
        lines.append(";;")
        lines.append(f"(defn {name} {args}")
        lines.append(f"  {default})")
        lines.append(";;")
    lines.append(";; Your code below")
    return "\n".join(lines) + "\n"


def make_test_file(ex) -> str:
    return (
        "(require '[clojure.test :refer [deftest is]])\n\n"
        + ex.test_body.strip()
        + "\n"
    )


def build_exercises():
    bank = _load_module("generate_content_bank")
    Exercise = bank.Exercise
    exs = []
    lv = "01-print-and-variables"

    level_one = [
        (
            "01-hello",
            "Print exactly `Hello, World!`",
            "Hello, World!",
            '(println "Hello, World!")',
            "",
        ),
        (
            "02-name-age",
            'GIVEN name = "Riya", age = 27. Print `Riya is 27 years old`.',
            "Riya is 27 years old",
            '(let [name "Riya"\n      age 27]\n  (println name "is" age "years old"))',
            '(def name "Riya")\n(def age 27)',
        ),
        (
            "03-two-lines",
            "Print `Line one` then `Line two` using two println calls.",
            "Line one\nLine two",
            '(println "Line one")\n(println "Line two")',
            "",
        ),
        (
            "04-one-log-two-lines",
            "Print the same two lines using one println and \\n.",
            "Line one\nLine two",
            '(println "Line one\\nLine two")',
            "",
        ),
        (
            "05-let-reassign",
            "Print count 10 then 20 using let shadowing (no reassignment).",
            "10\n20",
            "(let [count 10]\n  (println count)\n  (let [count 20]\n    (println count)))",
            "",
        ),
        (
            "06-typeof",
            'Print type labels for 5, "hi", true, nil, nil, {} using predicates.',
            "number\nstring\nboolean\nnil\nnil\nmap",
            textwrap.dedent(
                """
                (defn type-label [x]
                  (cond
                    (number? x) "number"
                    (string? x) "string"
                    (boolean? x) "boolean"
                    (nil? x) "nil"
                    (map? x) "map"
                    :else "other"))
                (doseq [v [5 "hi" true nil nil {}]]
                  (println (type-label v)))
                """
            ).strip(),
            "",
        ),
        (
            "07-concat",
            "GIVEN first/last. Print full name with a space.",
            "Ada Lovelace",
            '(let [first "Ada"\n      last "Lovelace"]\n  (println first last))',
            '(def first "Ada")\n(def last "Lovelace")',
        ),
        (
            "08-address",
            "Print 3-line address.",
            "12 Park Road\nBareilly\n243001",
            '(println "12 Park Road")\n(println "Bareilly")\n(println "243001")',
            "",
        ),
        (
            "09-swap",
            "Swap a and b with destructuring; print a=2 b=1.",
            "a=2 b=1",
            '(let [a 1 b 2 [a b] [b a]]\n  (println (str "a=" a " b=" b)))',
            "(def a 1)\n(def b 2)",
        ),
        (
            "10-decimals",
            "Print pi rounded to 2 decimals.",
            "3.14",
            '(let [pi 3.14159]\n  (println (format "%.2f" pi)))',
            "(def pi 3.14159)",
        ),
        (
            "11-booleans",
            'Print (> 5 3) and (= 5 "5").',
            "true\nfalse",
            '(println (> 5 3))\n(println (= 5 "5"))',
            "",
        ),
        (
            "12-escapes",
            "Print quoted sentence and tab-separated a\\tb.",
            'She said "hello" and left.\na\tb',
            '(println "She said \\"hello\\" and left.")\n(println "a\\tb")',
            "",
        ),
    ]
    for base, task, expected, sol, given in level_one:
        exs.append(Exercise(lv, base, task, expected, sol, given=given))

    exs.extend(bank.exercises())

    hints_mod = _load_module("exercise_hints")
    hint_map = hints_mod.HINTS
    for ex in exs:
        eid = f"{ex.level}/{ex.basename}"
        if eid not in hint_map:
            raise SystemExit(f"Missing hint for exercise: {eid}")
        if not hint_map[eid].strip():
            raise SystemExit(f"Empty hint for exercise: {eid}")
        ex.hint = hint_map[eid]
    return exs


def splice_level_file(level_path: Path, stub: str) -> None:
    """Replace comment header in a level exercise; keep learner code below marker."""
    marker = ";; Your code below"
    stub_idx = stub.find(marker)
    if stub_idx < 0:
        raise ValueError("stub missing ;; Your code below")
    header = stub[: stub_idx + len(marker)]

    if not level_path.exists():
        level_path.write_text(stub, encoding="utf-8")
        return
    content = level_path.read_text(encoding="utf-8")
    idx = content.find(marker)
    if idx < 0:
        level_path.write_text(stub, encoding="utf-8")
        return
    tail_start = idx + len(marker)
    if tail_start < len(content) and content[tail_start] == "\n":
        tail_start += 1
    tail = content[tail_start:]
    level_path.write_text(header + "\n" + tail, encoding="utf-8")


def refresh_headers() -> int:
    """Update stubs and level exercise headers with hints; preserve learner code."""
    root = REPO_ROOT
    exercises = build_exercises()
    count = 0
    for ex in exercises:
        stub = make_stub(ex)
        stub_path = root / "stubs" / ex.level / f"{ex.basename}.clj"
        level_path = root / "levels" / ex.level / f"{ex.basename}.clj"
        stub_path.parent.mkdir(parents=True, exist_ok=True)
        stub_path.write_text(stub, encoding="utf-8")
        count += 1
        if level_path.exists():
            splice_level_file(level_path, stub)
            count += 1
    return count


def write_all() -> int:
    count = 0
    root = REPO_ROOT
    exercises = build_exercises()

    expected_counts = sum(n for _, n in LEVEL_FOLDERS)
    if len(exercises) != expected_counts:
        raise SystemExit(
            f"Exercise count mismatch: got {len(exercises)}, expected {expected_counts}"
        )

    readmes = _load_module("generate_content_readmes").readmes()

    for ex in exercises:
        stub = make_stub(ex)
        level_dir = root / "levels" / ex.level
        stub_dir = root / "stubs" / ex.level
        sol_dir = root / ".solutions" / ex.level
        for d in (level_dir, stub_dir, sol_dir):
            d.mkdir(parents=True, exist_ok=True)

        for p, content in [
            (level_dir / f"{ex.basename}.clj", stub),
            (stub_dir / f"{ex.basename}.clj", stub),
            (sol_dir / f"{ex.basename}.clj", ex.solution + "\n"),
        ]:
            p.write_text(content, encoding="utf-8")
            count += 1

        for rel, content in ex.extra_solution_files.items():
            fp = sol_dir / rel
            fp.parent.mkdir(parents=True, exist_ok=True)
            fp.write_text(content + "\n", encoding="utf-8")
            count += 1

        if ex.basename in TEST_GRADED.get(ex.level, ()):
            tf = level_dir / f"{ex.basename}_test.clj"
            tf.write_text(make_test_file(ex), encoding="utf-8")
            count += 1

    for level, _ in LEVEL_FOLDERS:
        rp = root / "levels" / level / "README.md"
        rp.parent.mkdir(parents=True, exist_ok=True)
        rp.write_text(readmes[level], encoding="utf-8")
        count += 1

    sample = root / "levels" / "15-namespaces-effects" / "data" / "sample.txt"
    sample.parent.mkdir(parents=True, exist_ok=True)
    sample.write_text("hello from a file", encoding="utf-8")
    count += 1

    return count


def main() -> None:
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "refresh-headers":
        n = refresh_headers()
        print(f"Refreshed headers for {n} file writes")
        raise SystemExit(0)
    n = write_all()
    print(f"Wrote {n} files")
    raise SystemExit(0)


if __name__ == "__main__":
    main()
