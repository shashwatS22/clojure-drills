"""Level README.md bodies for generate_content.py."""

from __future__ import annotations


def _block(title: str, bullets: list[str], concepts: list[tuple[str, str, str]], mistakes: list[str], exercise_count: int) -> str:
    concept_md = ""
    for heading, explain, code in concepts:
        concept_md += f"\n### {heading}\n{explain}\n\n```clojure\n{code.strip()}\n```\n\n"
    mist = "\n".join(f"- {m}" for m in mistakes)
    learn = "\n".join(f"- {b}" for b in bullets)
    return f"""# {title}

## What you'll learn
{learn}

## Concepts
{concept_md}
## Common mistakes
{mist}

## Before you start
Type every example above into `playground/scratch.clj` and run it with Babashka. Change a number and predict what happens before you run it again.

## Exercises
Work through the numbered files in order. Save each file to check it with the watcher.
"""


def readmes() -> dict[str, str]:
    return {
        "01-print-and-variables": _block(
            "Level 01 — Print and variables",
            [
                "Printing lines with `println`",
                "Binding names with `def` and `let`",
                "Shadowing values without reassignment",
                "Checking types with `number?`, `string?`, and friends",
                "Building strings and simple output",
            ],
            [
                (
                    "println",
                    "Prints a line and adds a newline.",
                    '(println "Hello")\n;; Hello',
                ),
                (
                    "let shadowing",
                    "Use a new `let` to bind the same name to a new value.",
                    "(let [count 10]\n  (println count)\n  (let [count 20]\n    (println count)))\n;; 10\n;; 20",
                ),
                (
                    "Type predicates",
                    "Clojure uses predicates instead of JavaScript `typeof`.",
                    '(println (number? 5))\n(println (string? "hi"))\n;; true\n;; true',
                ),
            ],
            [
                "Trying to reassign a `let` binding — use another `let` instead.",
                "Forgetting quotes around strings.",
                "Using `print` when you need a full line (`println`).",
            ],
            12,
        ),
        "02-operators": _block(
            "Level 02 — Operators",
            [
                "Arithmetic and ratios like `17/5`",
                "Integer division with `quot` and remainders with `rem`/`mod`",
                "Logic with `and`, `or`, `not`",
                "Comparisons with `=`",
                "Parsing numbers from strings",
            ],
            [
                (
                    "Division",
                    "`(/ 17 5)` keeps an exact ratio.",
                    "(println (/ 17 5))\n;; 17/5",
                ),
                (
                    "rem vs mod",
                    "Remainders differ for negative numbers.",
                    "(println (rem -7 3))\n(println (mod -7 3))\n;; -1\n;; 2",
                ),
                (
                    "inc",
                    "Use `(inc x)` instead of `x++`.",
                    "(let [x 5]\n  (println (inc x)))\n;; 6",
                ),
            ],
            [
                "Using `/` when you wanted whole-number division — use `quot`.",
                "Confusing `rem` and `mod` on negative numbers.",
                "Concatenating strings with `+` — use `str` instead.",
            ],
            12,
        ),
        "03-conditionals": _block(
            "Level 03 — Conditionals",
            [
                "`if` for two-way choices",
                "`cond` for many conditions",
                "`case` for matching one value",
                "Truthy values — only `nil` and `false` are false",
            ],
            [
                (
                    "if",
                    "Pick one branch.",
                    '(if (> 3 1) (println "yes") (println "no"))\n;; yes',
                ),
                (
                    "cond",
                    "Like a chain of else-if.",
                    "(cond\n  (> n 0) (println \"positive\")\n  (< n 0) (println \"negative\")\n  :else (println \"zero\"))",
                ),
                (
                    "case",
                    "Match a single value.",
                    '(println (case day 1 "Mon" 2 "Tue" "other"))',
                ),
            ],
            [
                "Treating `0` or `\"\"` as false — in Clojure they are truthy.",
                "Forgetting the `:else` branch in `cond`.",
                "Using `case` without a default for unknown values.",
            ],
            12,
        ),
        "04-for-loops": _block(
            "Level 04 — Loops for printing and accumulating",
            [
                "`doseq` and `range` for counting loops",
                "`loop` / `recur` for sums and counters",
                "Building number results step by step",
            ],
            [
                (
                    "doseq",
                    "Run side effects like printing.",
                    "(doseq [i (range 1 4)]\n  (println i))\n;; 1\n;; 2\n;; 3",
                ),
                (
                    "loop / recur",
                    "Tail-recursive accumulation.",
                    "(loop [i 1 sum 0]\n  (if (> i 3)\n    (println sum)\n    (recur (inc i) (+ sum i))))\n;; 6",
                ),
            ],
            [
                "Using `recur` outside `loop`/`fn`.",
                "Infinite loops when the counter never moves toward the end condition.",
                "Using strings to count digits when the exercise forbids it.",
            ],
            14,
        ),
        "05-loop-recur": _block(
            "Level 05 — loop/recur drills",
            [
                "Digit extraction with `quot` and `rem`",
                "Classic while-style algorithms with `loop`/`recur`",
                "A do-while style drill that always runs once",
            ],
            [
                (
                    "Digit sum",
                    "Peel off the last digit until the number is zero.",
                    "(loop [n 482 sum 0]\n  (if (zero? n)\n    (println sum)\n    (recur (quot n 10) (+ sum (rem n 10)))))\n;; 14",
                ),
                (
                    "Run once",
                    "Print before checking, like do-while.",
                    '(println "ran once")\n(loop [once true]\n  (when once\n    (println "loop finished")\n    (recur false)))\n;; ran once\n;; loop finished',
                ),
            ],
            [
                "Forgetting to shrink `n` in digit loops.",
                "Using `/` on integers when you mean `quot`.",
            ],
            10,
        ),
        "06-patterns": _block(
            "Level 06 — Patterns",
            [
                "Nested loops for rows and columns",
                "Building one row string, then one `println` per row",
                "Padding with `format`",
            ],
            [
                (
                    "One println per row",
                    "Build the full row first.",
                    '(let [row (apply str (repeat 5 "*"))]\n  (println row))\n;; *****',
                ),
                (
                    "format padding",
                    "Pad numbers to a fixed width.",
                    '(println (format "%4d" 7))\n;;    7',
                ),
            ],
            [
                "Many `print` calls per row — build one string instead.",
                "Off-by-one row counts.",
                "Extra spaces at row ends.",
            ],
            16,
        ),
        "07-number-problems": _block(
            "Level 07 — Number problems",
            [
                "Digits, primes, divisors, GCD/LCM",
                "Boolean checks like palindrome and Armstrong numbers",
                "Frequency of digits",
            ],
            [
                (
                    "Digit count",
                    "Divide by 10 until zero.",
                    "(loop [n 946 c 0]\n  (if (zero? n) (println c) (recur (quot n 10) (inc c))))\n;; 3",
                ),
                (
                    "Prime check",
                    "Try divisors up to sqrt(n).",
                    "(println (not (some #(zero? (rem 97 %)) (range 2 10))))\n;; true",
                ),
            ],
            [
                "Checking primality with a loop to `n` instead of `sqrt(n)`.",
                "Dropping leading zeros when reversing (700 → 7).",
            ],
            14,
        ),
        "08-functions": _block(
            "Level 08 — Functions",
            [
                "`defn`, anonymous `#()` fns, multi-arity",
                "Variadic args with `&`",
                "`apply` and higher-order functions",
                "Atoms for mutable counter state",
                "`prn` to show return vs side-effect printing",
            ],
            [
                (
                    "defn",
                    "Named function with parameters.",
                    "(defn add [a b] (+ a b))\n(println (add 2 3))\n;; 5",
                ),
                (
                    "apply",
                    "Call a function with a collection of args.",
                    "(println (apply max [4 9 2]))\n;; 9",
                ),
                (
                    "atom counter",
                    "Swap an atom for increasing state.",
                    "(let [n (atom 0)] (swap! n inc) (println @n))\n;; 1",
                ),
            ],
            [
                "Confusing `println` (side effect) with the return value — use `prn` to inspect.",
                "Forgetting base case in higher-order helpers.",
            ],
            14,
        ),
        "09-strings": _block(
            "Level 09 — Strings",
            [
                "`clojure.string` helpers",
                "Immutability — strings are not changed in place",
                "Subs, replace, split, join",
            ],
            [
                (
                    "subs",
                    "Slice-like substring.",
                    '(println (subs "abcdefgh" 2 5))\n;; cde',
                ),
                (
                    "split / join",
                    "Break apart and rejoin.",
                    '(require \'[clojure.string :as str])\n(println (str/join "-" (str/split "a,b" #",")))\n;; a-b',
                ),
            ],
            [
                "Using JavaScript-only methods — use `clojure.string` instead.",
                "Forgetting that strings are seq-able character by character.",
            ],
            14,
        ),
        "10-vectors": _block(
            "Level 10 — Vectors",
            [
                "Immutable vectors with `conj`, `pop`, `peek`",
                "Indexing, subvec, and loops",
                "Classic array-style drills without mutation",
            ],
            [
                (
                    "conj",
                    "Adds at the end, returns a new vector.",
                    "(println (conj [1 2] 3))\n;; [1 2 3]",
                ),
                (
                    "peek / pop",
                    "Look at or remove the last element.",
                    "(println (peek [1 2 3]))\n(println (pop [1 2 3]))\n;; 3\n;; [1 2]",
                ),
            ],
            [
                "Expecting `conj` to mutate the original vector.",
                "Using `first` when you meant the last element — use `peek` or `last`.",
            ],
            16,
        ),
        "11-seq-transforms": _block(
            "Level 11 — Sequence transforms",
            [
                "`map`, `filter`, `reduce`",
                "`sort` and `sort-by`",
                "Threading with `->>`",
                "One-level vs full flatten",
            ],
            [
                (
                    "map / filter",
                    "Transform or keep elements.",
                    "(println (map inc [1 2 3]))\n;; (2 3 4)",
                ),
                (
                    "->>",
                    "Thread a collection through steps.",
                    "(->> [1 2 3 4] (filter even?) (map #(* % %)) (reduce +))\n;; 20",
                ),
            ],
            [
                "Using `flatten` when you only need one level.",
                "Sorting numbers as strings — use `sort` on numbers directly.",
            ],
            12,
        ),
        "12-maps": _block(
            "Level 12 — Maps",
            [
                "Keywords as keys",
                "`assoc`, `dissoc`, `merge`",
                "JSON with Cheshire",
                "Safe access with `get-in`",
            ],
            [
                (
                    "Keyword keys",
                    "Keywords are the usual map keys.",
                    '(let [user {:name "Ada"}]\n  (println (:name user)))\n;; Ada',
                ),
                (
                    "merge",
                    "Combine maps; right-hand values win.",
                    '(println (:b (merge {:a 1 :b 2} {:b 3})))\n;; 3',
                ),
            ],
            [
                "Using string keys when the data uses keywords.",
                "Forgetting Cheshire generates JSON without extra spaces.",
            ],
            12,
        ),
        "13-recursion": _block(
            "Level 13 — Recursion",
            [
                "Base case and recursive case",
                "Using `recur` for tail recursion",
                "Thinking in return values (tests on later exercises)",
            ],
            [
                (
                    "factorial stack",
                    "Each call waits for the next.",
                    ";; (factorial 4)\n;; → (* 4 (factorial 3))\n;; → (* 4 (* 3 (factorial 2)))\n;; → … until factorial 1 → 1",
                ),
                (
                    "sum-to",
                    "Classic downward recursion.",
                    "(defn sum-to [n]\n  (if (<= n 1) n (+ n (sum-to (dec n)))))\n(println (sum-to 5))\n;; 15",
                ),
            ],
            [
                "Missing base case → stack overflow.",
                "Using loops when the exercise asks for recursion.",
            ],
            10,
        ),
        "14-frequency": _block(
            "Level 14 — Frequency and sets",
            [
                "`frequencies`, `update`, `fnil`",
                "`clojure.set` union and intersection",
                "Counting for anagram and two-sum style problems",
            ],
            [
                (
                    "frequencies",
                    "Count occurrences in one pass.",
                    '(println (frequencies "banana"))\n;; {\\a 3, \\b 1, \\n 2}',
                ),
                (
                    "set ops",
                    "Union and intersection.",
                    "(require '[clojure.set :as set])\n(println (set/union #{1 2} #{2 3}))\n;; #{1 2 3}",
                ),
            ],
            [
                "Losing insertion order when printing counts — follow the exercise pattern.",
                "Building frequency maps by hand when `frequencies` fits.",
            ],
            10,
        ),
        "15-namespaces-effects": _block(
            "Level 15 — Namespaces and effects",
            [
                "`require` and namespaces",
                "`try` / `catch` / `finally` and `ex-info`",
                "`future`, `promise`, `delay`",
                "Reading files with `slurp`",
            ],
            [
                (
                    "require",
                    "Load code from another namespace.",
                    "(require '[clojure.string :as str])\n(println (str/upper-case \"ada\"))\n;; ADA",
                ),
                (
                    "try / catch",
                    "Handle errors without crashing.",
                    '(try (/ 1 0) (catch Exception _ (println "caught")))\n;; caught',
                ),
                (
                    "slurp",
                    "Read a whole file.",
                    '(println (slurp "levels/15-namespaces-effects/data/sample.txt"))\n;; hello from a file',
                ),
            ],
            [
                "Wrong namespace name in `require`.",
                "Blocking forever on a promise that is never delivered.",
            ],
            12,
        ),
    }
