"""Exercise definitions for levels 02–15 (loaded by generate_content.py)."""

from __future__ import annotations

import textwrap
from dataclasses import dataclass, field
from typing import Callable, Optional


@dataclass
class Exercise:
    level: str
    basename: str
    task: str
    expected: str
    solution: str
    given: str = ""
    hint: str = ""
    fn_stub: Optional[tuple[str, str, str]] = None
    test_body: str = ""
    extra_solution_files: dict[str, str] = field(default_factory=dict)


def clj_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def solution_doseq_println(lines: list[str]) -> str:
    inner = "\n".join(f"    {clj_str(line)}" for line in lines)
    return f"(doseq [line [{inner}]]\n  (println line))"


def star_square(n=5):
    return ["*" * n for _ in range(n)]


def star_triangle(n=5):
    return ["*" * i for i in range(1, n + 1)]


def number_triangle(n=5):
    return [" ".join(str(j) for j in range(1, i + 1)) for i in range(1, n + 1)]


def same_number_triangle(n=5):
    return [" ".join(str(i) for _ in range(i)) for i in range(1, n + 1)]


def inverted_star_triangle(n=5):
    return ["*" * i for i in range(n, 0, -1)]


def inverted_number_triangle(n=5):
    return [" ".join(str(j) for j in range(1, i + 1)) for i in range(n, 0, -1)]


def floyds_triangle(n=5):
    lines, num, row = [], 1, 1
    while row <= n:
        parts = []
        for _ in range(row):
            parts.append(str(num))
            num += 1
        lines.append(" ".join(parts))
        row += 1
    return lines


def binary_triangle(n=5):
    return [
        " ".join("1" if j % 2 == 0 else "0" for j in range(i))
        for i in range(1, n + 1)
    ]


def centred_pyramid(n=5):
    lines, width = [], 2 * n - 1
    for i in range(1, n + 1):
        stars = 2 * i - 1
        lines.append(" " * ((width - stars) // 2) + "*" * stars)
    return lines


def inverted_centred_pyramid(n=5):
    lines, width = [], 2 * n - 1
    for i in range(n, 0, -1):
        stars = 2 * i - 1
        lines.append(" " * ((width - stars) // 2) + "*" * stars)
    return lines


def diamond(n=5):
    return centred_pyramid(n) + inverted_centred_pyramid(n)[1:]


def half_diamond(n=5):
    return star_triangle(n) + inverted_star_triangle(n)[1:]


def butterfly(n=4):
    lines = []
    for i in list(range(1, n + 1)) + list(range(n - 1, 0, -1)):
        left = "*" * i
        lines.append(left + " " * (2 * (n - i)) + left)
    return lines


def hollow_square(n=5):
    return [
        "*" * n if i in (0, n - 1) else "*" + " " * (n - 2) + "*"
        for i in range(n)
    ]


def alphabet_triangle(n=5):
    return [
        " ".join(chr(ord("A") + j) for j in range(i)) for i in range(1, n + 1)
    ]


def multiplication_grid(n=5):
    return ["".join(f"{i * j:4d}" for j in range(1, n + 1)) for i in range(1, n + 1)]


PATTERN_BUILDERS: list[tuple[str, Callable[[], list[str]]]] = [
    ("01-star-square", lambda: star_square(5)),
    ("02-star-triangle", lambda: star_triangle(5)),
    ("03-number-triangle", lambda: number_triangle(5)),
    ("04-same-number-triangle", lambda: same_number_triangle(5)),
    ("05-inverted-star-triangle", lambda: inverted_star_triangle(5)),
    ("06-inverted-number-triangle", lambda: inverted_number_triangle(5)),
    ("07-floyds-triangle", lambda: floyds_triangle(5)),
    ("08-binary-triangle", lambda: binary_triangle(5)),
    ("09-pyramid", lambda: centred_pyramid(5)),
    ("10-inverted-pyramid", lambda: inverted_centred_pyramid(5)),
    ("11-diamond", lambda: diamond(5)),
    ("12-half-diamond", lambda: half_diamond(5)),
    ("13-butterfly", lambda: butterfly(4)),
    ("14-hollow-square", lambda: hollow_square(5)),
    ("15-alphabet-triangle", lambda: alphabet_triangle(5)),
    ("16-multiplication-grid", lambda: multiplication_grid(5)),
]

PEOPLE = (
    '[{:name "Ada" :age 36 :city "London"}\n'
    ' {:name "Raman" :age 42 :city "Kolkata"}\n'
    ' {:name "Meera" :age 29 :city "Pune"}]'
)


def fizzbuzz_line(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def exercises() -> list:
    exs = []
    lv = "02-operators"

    exs += [
        Exercise(
            lv,
            "01-arithmetic",
            "GIVEN a = 17, b = 5. Print sum, difference, product, quotient (/), remainder (rem) — one per line.",
            "22\n12\n85\n17/5\n2",
            "(let [a 17\n      b 5]\n  (println (+ a b))\n  (println (- a b))\n  (println (* a b))\n  (println (/ a b))\n  (println (rem a b)))",
            given="(def a 17)\n(def b 5)",
        ),
        Exercise(
            lv,
            "02-integer-divide",
            "GIVEN a = 17, b = 5. Print the whole-number part using quot.",
            "3",
            "(let [a 17\n      b 5]\n  (println (quot a b)))",
            given="(def a 17)\n(def b 5)",
        ),
        Exercise(
            lv,
            "03-post-vs-pre",
            "GIVEN x = 5. Simulate post-increment and pre-increment using inc and let (print values like JS x++/++x).",
            "5\n6\n7\n7",
            "(let [x 5]\n  (println x)\n  (let [x (inc x)]\n    (println x)\n    (let [x (inc x)]\n      (println x)\n      (println x))))",
            given="(def x 5)",
        ),
        Exercise(
            lv,
            "04-compound",
            "GIVEN total = 100. Apply +20, -30, *2, /4 in order using let shadowing, printing after each step.",
            "120\n90\n180\n45",
            "(let [total 100]\n  (let [total (+ total 20)] (println total)\n    (let [total (- total 30)] (println total)\n      (let [total (* total 2)] (println total)\n        (let [total (/ total 4)] (println total))))))",
            given="(def total 100)",
        ),
        Exercise(
            lv,
            "05-loose-vs-strict",
            "Print results of = comparisons that mirror JS == vs === (adapted for Clojure).",
            "true\nfalse\ntrue\nfalse\ntrue\nfalse",
            textwrap.dedent(
                """
                (println (= 1 "1"))
                (println (= 1 (Integer/parseInt "1")))
                (println (= 0 false))
                (println (= 0 (if false 1 0)))
                (println (= nil nil))
                (println (not= nil false))
                """
            ).strip(),
        ),
        Exercise(
            lv,
            "06-logical",
            "GIVEN a = true, b = false. Print a and b, a or b, (not a), (not b).",
            "false\ntrue\nfalse\ntrue",
            "(let [a true\n      b false]\n  (println (and a b))\n  (println (or a b))\n  (println (not a))\n  (println (not b)))",
            given="(def a true)\n(def b false)",
        ),
        Exercise(
            lv,
            "07-ternary",
            "Print rem and mod for -7 and 3 (replaces JS ternary drill).",
            "-1\n2",
            "(println (rem -7 3))\n(println (mod -7 3))",
        ),
        Exercise(
            lv,
            "08-string-to-number",
            'GIVEN s = "42". Print (str s 8) and (+ (parse-long s) 8).',
            "428\n50",
            '(let [s "42"]\n  (println (str s 8))\n  (println (+ (parse-long s) 8)))',
            given='(def s "42")',
        ),
        Exercise(
            lv,
            "09-nan",
            'GIVEN invalid parse. Use parse-long on "abc", print the value with prn, then print (nil? x).',
            "nil\ntrue",
            '(let [x (parse-long "abc")]\n  (prn x)\n  (println (nil? x)))',
        ),
        Exercise(
            lv,
            "10-math-methods",
            "Print abs(-7), 2^10, sqrt(144), round 4.6, max of 3 9 2.",
            "7\n1024\n12.0\n5.0\n9",
            textwrap.dedent(
                """
                (println (Math/abs -7))
                (println (Math/pow 2 10))
                (println (Math/sqrt 144))
                (println (Math/round 4.6))
                (println (max 3 9 2))
                """
            ).strip(),
        ),
        Exercise(
            lv,
            "11-precedence",
            "Print 2 + 3 * 4, (2 + 3) * 4, and 10 - 4 - 3.",
            "14\n20\n3",
            "(println (+ 2 (* 3 4)))\n(println (* (+ 2 3) 4))\n(println (- (- 10 4) 3))",
        ),
        Exercise(
            lv,
            "12-last-digit",
            "GIVEN n = 4739. Print last digit with rem, then first digit using quot (no loops).",
            "9\n4",
            "(let [n 4739]\n  (println (rem n 10))\n  (println (quot n 1000)))",
            given="(def n 4739)",
        ),
    ]

    lv = "03-conditionals"
    exs += [
        Exercise(lv, "01-sign", "GIVEN n = -14. Print positive, negative, or zero.", "negative",
                 "(let [n -14]\n  (cond\n    (pos? n) (println \"positive\")\n    (neg? n) (println \"negative\")\n    :else (println \"zero\")))", given="(def n -14)"),
        Exercise(lv, "02-even-odd", "GIVEN n = 27. Print even or odd.", "odd",
                 "(let [n 27]\n  (if (even? n) (println \"even\") (println \"odd\")))", given="(def n 27)"),
        Exercise(lv, "03-max-of-two", "GIVEN a = 34, b = 34. Print larger or equal.", "equal",
                 "(let [a 34 b 34]\n  (cond\n    (> a b) (println a)\n    (> b a) (println b)\n    :else (println \"equal\")))", given="(def a 34)\n(def b 34)"),
        Exercise(lv, "04-max-of-three", "GIVEN a = 12, b = 45, c = 45. Print the largest.", "45",
                 "(let [a 12 b 45 c 45]\n  (println (max a b c)))", given="(def a 12)\n(def b 45)\n(def c 45)"),
        Exercise(lv, "05-leap-year", "GIVEN year = 2100. Print leap or not leap.", "not leap",
                 "(let [year 2100]\n  (println (if (and (zero? (rem year 4))\n                      (or (not (zero? (rem year 100))) (zero? (rem year 400))))\n                 \"leap\" \"not leap\")))", given="(def year 2100)"),
        Exercise(lv, "06-grade", "GIVEN marks = 73. Print letter grade.", "C",
                 "(let [marks 73]\n  (cond\n    (>= marks 90) (println \"A\")\n    (>= marks 75) (println \"B\")\n    (>= marks 60) (println \"C\")\n    (>= marks 40) (println \"D\")\n    :else (println \"F\")))", given="(def marks 73)"),
        Exercise(lv, "07-vowel", 'GIVEN ch = "u". Print vowel or consonant.', "vowel",
                 '(let [ch "u"]\n  (println (if (#{\\a \\e \\i \\o \\u} (first ch)) "vowel" "consonant")))', given='(def ch "u")'),
        Exercise(lv, "08-switch-day", "GIVEN day = 6. Use case to print weekday (1 = Monday).", "Saturday",
                 "(let [day 6]\n  (println (case day 1 \"Monday\" 2 \"Tuesday\" 3 \"Wednesday\" 4 \"Thursday\"\n                 5 \"Friday\" 6 \"Saturday\" 7 \"Sunday\" \"unknown\")))", given="(def day 6)"),
        Exercise(lv, "09-switch-calc", 'GIVEN a = 12, b = 4, op = "/". Use case on op.', "3",
                 '(let [a 12 b 4 op "/"]\n  (println (case op "+" (+ a b) "-" (- a b) "*" (* a b) "/" (/ a b) "unknown")))',
                 given='(def a 12)\n(def b 4)\n(def op "/")'),
        Exercise(lv, "10-can-vote", "GIVEN age = 17, isCitizen = true. Print can vote or cannot vote.", "cannot vote",
                 "(let [age 17 is-citizen true]\n  (println (if (and (>= age 18) is-citizen) \"can vote\" \"cannot vote\")))",
                 given="(def age 17)\n(def is-citizen true)"),
        Exercise(lv, "11-triangle-valid", "GIVEN sides 3, 4, 8. Print valid or invalid.", "invalid",
                 "(let [a 3 b 4 c 8]\n  (println (if (and (> (+ a b) c) (> (+ b c) a) (> (+ c a) b)) \"valid\" \"invalid\")))",
                 given="(def a 3)\n(def b 4)\n(def c 8)"),
        Exercise(lv, "12-fizzbuzz-one", "GIVEN n = 15. Print FizzBuzz, Fizz, Buzz, or the number.", "FizzBuzz",
                 "(let [n 15]\n  (println (cond\n             (zero? (rem n 15)) \"FizzBuzz\"\n             (zero? (rem n 3)) \"Fizz\"\n             (zero? (rem n 5)) \"Buzz\"\n             :else (str n))))", given="(def n 15)"),
    ]

    lv = "04-for-loops"
    exs.append(Exercise(lv, "01-one-to-ten", "Print 1 to 10, one per line.", "1\n2\n3\n4\n5\n6\n7\n8\n9\n10",
                          "(doseq [i (range 1 11)] (println i))"))
    exs.append(Exercise(lv, "02-ten-to-one", "Print 10 down to 1.", "10\n9\n8\n7\n6\n5\n4\n3\n2\n1",
                          "(doseq [i (range 10 0 -1)] (println i))"))
    evens = "\n".join(str(i) for i in range(2, 21, 2))
    exs.append(Exercise(lv, "03-evens", "Print even numbers 2 to 20.", evens,
                          "(doseq [i (range 2 21 2)] (println i))"))
    exs.append(Exercise(lv, "04-sum-to-n", "GIVEN n = 100. Print sum 1..n with loop/recur.", "5050",
                          "(let [n 100]\n  (loop [i 1 sum 0]\n    (if (> i n) (println sum)\n      (recur (inc i) (+ sum i)))))", given="(def n 100)"))
    tt = "\n".join(f"7 x {i} = {7 * i}" for i in range(1, 11))
    exs.append(Exercise(lv, "05-times-table", "GIVEN n = 7. Print times table 1..10.", tt,
                          "(let [n 7]\n  (doseq [i (range 1 11)] (println n \"x\" i \"=\" (* n i))))", given="(def n 7)"))
    exs.append(Exercise(lv, "06-factorial", "GIVEN n = 6. Print factorial using loop/recur.", "720",
                          "(let [n 6]\n  (loop [i 2 acc 1]\n    (if (> i n) (println acc)\n      (recur (inc i) (* acc i)))))", given="(def n 6)"))
    exs.append(Exercise(lv, "07-count-digits", "GIVEN n = 74821. Count digits with loop (no str).", "5",
                          "(let [n 74821]\n  (loop [x n c 0]\n    (if (zero? x) (println c)\n      (recur (quot x 10) (inc c)))))", given="(def n 74821)"))
    exs.append(Exercise(lv, "08-reverse-number", "GIVEN n = 12345. Reverse as number.", "54321",
                          "(let [n 12345]\n  (loop [x n rev 0]\n    (if (zero? x) (println rev)\n      (recur (quot x 10) (+ (* rev 10) (rem x 10))))))", given="(def n 12345)"))
    exs.append(Exercise(lv, "09-power", "GIVEN base = 3, exp = 5. Power with loop.", "243",
                          "(let [base 3 exp 5]\n  (loop [e exp acc 1]\n    (if (zero? e) (println acc)\n      (recur (dec e) (* acc base)))))", given="(def base 3)\n(def exp 5)"))
    exs.append(Exercise(lv, "10-sum-of-digits", "GIVEN n = 9375. Sum digits.", "24",
                          "(let [n 9375]\n  (loop [x n sum 0]\n    (if (zero? x) (println sum)\n      (recur (quot x 10) (+ sum (rem x 10))))))", given="(def n 9375)"))
    squares = "\n".join(str(i * i) for i in range(1, 9))
    exs.append(Exercise(lv, "11-squares", "Print squares 1..8.", squares,
                          "(doseq [i (range 1 9)] (println (* i i)))"))
    fib = [0, 1]
    while len(fib) < 10:
        fib.append(fib[-1] + fib[-2])
    exs.append(Exercise(lv, "12-fibonacci", "GIVEN n = 10. Print first n Fibonacci numbers.", "\n".join(map(str, fib)),
                          "(let [n 10]\n  (loop [count 0 a 0 b 1]\n    (when (< count n)\n      (println a)\n      (recur (inc count) b (+ a b)))))", given="(def n 10)"))
    fb = "\n".join(fizzbuzz_line(i) for i in range(1, 21))
    exs.append(Exercise(lv, "13-fizzbuzz", "FizzBuzz 1..20.", fb,
                          "(doseq [i (range 1 21)] (println (cond (zero? (rem i 15)) \"FizzBuzz\" (zero? (rem i 3)) \"Fizz\" (zero? (rem i 5)) \"Buzz\" :else i)))"))
    exs.append(Exercise(lv, "14-count-vowels", 'GIVEN s = "javascript is fun". Count vowels.', "6",
                          '(let [s "javascript is fun"]\n  (loop [chars (seq s) c 0]\n    (if (empty? chars) (println c)\n      (let [ch (first chars)]\n        (recur (rest chars) (if (#{\\a \\e \\i \\o \\u} ch) (inc c) c))))))',
                          given='(def s "javascript is fun")'))

    lv = "05-loop-recur"
    exs += [
        Exercise(lv, "01-while-count", "GIVEN n = 5. Print 1..n with loop/recur.", "1\n2\n3\n4\n5",
                 "(let [n 5]\n  (loop [i 1]\n    (when (<= i n)\n      (println i)\n      (recur (inc i)))))", given="(def n 5)"),
        Exercise(lv, "02-sum-digits-while", "GIVEN n = 48291. Digit sum with loop/recur.", "24",
                 "(let [n 48291]\n  (loop [x n sum 0]\n    (if (zero? x) (println sum)\n      (recur (quot x 10) (+ sum (rem x 10))))))", given="(def n 48291)"),
        Exercise(lv, "03-reverse-while", "GIVEN n = 9081. Reverse with loop/recur.", "1809",
                 "(let [n 9081]\n  (loop [x n rev 0]\n    (if (zero? x) (println rev)\n      (recur (quot x 10) (+ (* rev 10) (rem x 10))))))", given="(def n 9081)"),
        Exercise(lv, "04-palindrome-number", "GIVEN n = 12321. Print palindrome or not palindrome.", "palindrome",
                 "(let [n 12321 orig n rev 0]\n  (loop [x n rev 0]\n    (if (zero? x)\n      (println (if (= orig rev) \"palindrome\" \"not palindrome\"))\n      (recur (quot x 10) (+ (* rev 10) (rem x 10))))))", given="(def n 12321)"),
        Exercise(lv, "05-armstrong", "GIVEN n = 153. Print armstrong if sum of cubes of digits equals n.", "armstrong",
                 "(let [n 153]\n  (loop [x n sum 0]\n    (if (zero? x)\n      (println (if (= sum n) \"armstrong\" \"not armstrong\"))\n      (let [d (rem x 10)]\n        (recur (quot x 10) (+ sum (* d d d)))))))", given="(def n 153)"),
        Exercise(lv, "06-gcd", "GIVEN a = 48, b = 18. GCD with loop/recur.", "6",
                 "(let [a 48 b 18]\n  (loop [x a y b]\n    (if (zero? y) (println x)\n      (recur y (rem x y)))))", given="(def a 48)\n(def b 18)"),
        Exercise(lv, "07-count-digits-while", "GIVEN n = 1000000. Count digits.", "7",
                 "(let [n 1000000]\n  (loop [x n c 0]\n    (if (zero? x) (println c)\n      (recur (quot x 10) (inc c)))))", given="(def n 1000000)"),
        Exercise(lv, "08-to-binary", "GIVEN n = 25. Binary via divide by 2.", "11001",
                 "(let [n 25]\n  (loop [x n bits ()]\n    (if (zero? x)\n      (println (apply str (reverse bits)))\n      (recur (quot x 2) (conj bits (rem x 2))))))", given="(def n 25)"),
        Exercise(lv, "09-do-while", "GIVEN n = 0. Show body runs once (do-while style with loop/recur).", "ran once\nloop finished",
                 "(let [n 0]\n  (println \"ran once\")\n  (loop [once true]\n    (when once\n      (println \"loop finished\")\n      (recur false))))", given="(def n 0)"),
        Exercise(lv, "10-collatz", "GIVEN n = 27. Collatz steps to reach 1.", "111",
                 "(let [n 27]\n  (loop [x n steps 0]\n    (if (= x 1) (println steps)\n      (recur (if (even? x) (/ x 2) (+ (* 3 x) 1)) (inc steps)))))", given="(def n 27)"),
    ]

    lv = "06-patterns"
    for base, builder in PATTERN_BUILDERS:
        lines = builder()
        exs.append(
            Exercise(
                lv,
                base,
                f"Print the pattern (see expected output). GIVEN n = 5 unless noted.",
                "\n".join(lines),
                solution_doseq_println(lines),
                given="(def n 5)",
            )
        )

    lv = "07-number-problems"
    exs += [
        Exercise(lv, "01-count-digits", "GIVEN n = 946213. Digit count.", "6",
                 "(let [n 946213]\n  (loop [x n c 0]\n    (if (zero? x) (println c) (recur (quot x 10) (inc c)))))", given="(def n 946213)"),
        Exercise(lv, "02-reverse", "GIVEN n = 700. Reverse number.", "7",
                 "(let [n 700]\n  (loop [x n rev 0]\n    (if (zero? x) (println rev) (recur (quot x 10) (+ (* rev 10) (rem x 10))))))", given="(def n 700)"),
        Exercise(lv, "03-palindrome", "GIVEN n = 1221. Print true/false.", "true",
                 "(let [n 1221 orig n]\n  (loop [x n rev 0]\n    (if (zero? x) (println (= orig rev)) (recur (quot x 10) (+ (* rev 10) (rem x 10))))))", given="(def n 1221)"),
        Exercise(lv, "04-armstrong", "GIVEN n = 371. Armstrong true/false.", "true",
                 "(let [n 371 digits (loop [x n ds []] (if (zero? x) ds (recur (quot x 10) (conj ds (rem x 10)))))]\n  (println (= n (reduce + (map #(* % % %) digits)))))", given="(def n 371)"),
        Exercise(lv, "05-divisors", "GIVEN n = 36. Print divisors space-separated.", "1 2 3 4 6 9 12 18 36",
                 "(let [n 36]\n  (println (clojure.string/join \" \" (filter #(zero? (rem n %)) (range 1 (inc n))))))", given="(def n 36)"),
        Exercise(lv, "06-is-prime", "GIVEN n = 97. Print prime or not prime.", "prime",
                 "(let [n 97\n      prime? (and (> n 1)\n                  (not (some #(zero? (rem n %))\n                             (range 2 (inc (int (Math/sqrt n))))))]\n  (println (if prime? \"prime\" \"not prime\")))", given="(def n 97)"),
        Exercise(lv, "07-gcd", "GIVEN a = 120, b = 45.", "15",
                 "(let [a 120 b 45]\n  (loop [x a y b] (if (zero? y) (println x) (recur y (rem x y)))))", given="(def a 120)\n(def b 45)"),
        Exercise(lv, "08-lcm", "GIVEN a = 12, b = 18. LCM.", "36",
                 "(let [a 12 b 18 gcd (loop [x a y b] (if (zero? y) x (recur y (rem x y))))]\n  (println (/ (* a b) gcd)))", given="(def a 12)\n(def b 18)"),
        Exercise(lv, "09-sum-divisors", "GIVEN n = 28. Sum of divisors.", "56",
                 "(let [n 28]\n  (println (reduce + (filter #(zero? (rem n %)) (range 1 (inc n))))))", given="(def n 28)"),
        Exercise(lv, "10-perfect-number", "GIVEN n = 496. Print perfect if proper divisors sum to n.", "perfect",
                 "(let [n 496 sum-proper (reduce + (filter #(and (zero? (rem n %)) (not= % n)) (range 1 n)))]\n  (println (if (= sum-proper n) \"perfect\" \"not perfect\")))", given="(def n 496)"),
        Exercise(lv, "11-prime-factors", "GIVEN n = 360. Prime factors with repeats.", "2 2 2 3 3 5",
                 "(let [n 360]\n  (loop [x n d 2 factors []]\n    (cond\n      (= x 1) (println (clojure.string/join \" \" factors))\n      (zero? (rem x d)) (recur (quot x d) d (conj factors d))\n      :else (recur x (inc d) factors))))", given="(def n 360)"),
        Exercise(lv, "12-primes-to-n", "GIVEN n = 30. Primes up to n.", "2 3 5 7 11 13 17 19 23 29",
                 "(let [n 30 prime? (fn [x] (and (> x 1) (not (some #(zero? (rem x %)) (range 2 (inc (int (Math/sqrt x))))))))]\n  (println (clojure.string/join \" \" (filter prime? (range 2 (inc n))))))", given="(def n 30)"),
        Exercise(lv, "13-nth-prime", "GIVEN k = 20. Print 20th prime.", "71",
                 "(let [k 20 prime? (fn [x] (and (> x 1) (not (some #(zero? (rem x %)) (range 2 (inc (int (Math/sqrt x))))))))]\n  (println (nth (filter prime? (range 2)) (dec k))))", given="(def k 20)"),
        Exercise(lv, "14-digit-frequency", "GIVEN n = 1223334444. Print digit:count ascending.", "1:1 2:2 3:3 4:4",
                 '(let [n 1223334444 s (str n) freqs (frequencies s)]\n  (println (clojure.string/join " " (map (fn [[d c]] (str d ":" c)) (sort freqs)))))', given="(def n 1223334444)"),
    ]

    lv = "08-functions"
    exs += [
        Exercise(lv, "01-add", "Export add(a,b) returning sum.", "tests",
                 "(defn add [a b]\n  (+ a b))",
                 fn_stub=("add", "[a b]", "nil"),
                 test_body=textwrap.dedent("""
                    (deftest add-test
                      (is (= (add 2 3) 5))
                      (is (= (add -1 1) 0)))
                 """)),
        Exercise(lv, "02-arrow-multiply", "Export multiply using #() anonymous fn.", "tests",
                 "(def multiply #(* %1 %2))",
                 fn_stub=("multiply", "[a b]", "nil"),
                 test_body="(deftest multiply-test\n  (is (= (multiply 3 4) 12))\n  (is (= (multiply -2 5) -10)))"),
        Exercise(lv, "03-default-params", "Export greet with default greeting Hello.", "tests",
                 '(defn greet ([name] (greet name "Hello"))\n  ([name greeting] (str greeting ", " name "!")))',
                 fn_stub=("greet", "[name] or [name greeting]", "nil"),
                 test_body='(deftest greet-test\n  (is (= (greet "Ada") "Hello, Ada!"))\n  (is (= (greet "Ada" "Hi") "Hi, Ada!")))'),
        Exercise(lv, "04-is-even", "Export is-even returning boolean.", "tests",
                 "(defn is-even [n] (even? n))",
                 fn_stub=("is-even", "[n]", "false"),
                 test_body="(deftest is-even-test\n  (is (is-even 4))\n  (is (not (is-even 7))))"),
        Exercise(lv, "05-min-max-object", "Export min-max returning map with :min :max.", "tests",
                 "(defn min-max [numbers]\n  {:min (apply min numbers)\n   :max (apply max numbers)})",
                 fn_stub=("min-max", "[numbers]", "{:min 0 :max 0}"),
                 test_body="(deftest min-max-test\n  (is (= (min-max [3 1 9]) {:min 1 :max 9})))"),
        Exercise(lv, "06-rest-sum", "Export sum with variadic args.", "tests",
                 "(defn sum\n  ([] 0)\n  ([x & xs] (reduce + x xs)))",
                 fn_stub=("sum", "([& numbers])", "0"),
                 test_body="(deftest sum-test\n  (is (= (sum) 0))\n  (is (= (sum 1 2 3) 6)))"),
        Exercise(lv, "07-apply-twice", "Export apply-twice.", "tests",
                 "(defn apply-twice [f value] (f (f value)))",
                 fn_stub=("apply-twice", "[f value]", "nil"),
                 test_body="(deftest apply-twice-test\n  (is (= (apply-twice inc 3) 5)))"),
        Exercise(lv, "08-make-multiplier", "Export make-multiplier.", "tests",
                 "(defn make-multiplier [n] #(* % n))",
                 fn_stub=("make-multiplier", "[n]", "nil"),
                 test_body="(deftest make-multiplier-test\n  (let [double (make-multiplier 2)]\n    (is (= (double 5) 10))))"),
        Exercise(lv, "09-return-vs-log", "Show return vs print — use prn for nil.", "5\n5\nnil",
                 "(defn returns-five [] 5)\n(defn prints-five [] (println 5))\n(prn (returns-five))\n(prints-five)\n(prn (prints-five))"),
        Exercise(lv, "10-spread-call", "GIVEN nums. apply max.", "9",
                 "(let [nums [4 9 2]]\n  (println (apply max nums)))", given="(def nums [4 9 2])"),
        Exercise(lv, "11-callback", "repeat times calling callback with index.", "step 0\nstep 1\nstep 2",
                 "(defn repeat-callback [times f]\n  (doseq [i (range times)] (f i)))\n(repeat-callback 3 #(println \"step\" %))"),
        Exercise(lv, "12-iife", "IIFE via ((fn [] ...)).", "ran immediately",
                 "((fn [] (println \"ran immediately\")))"),
        Exercise(lv, "13-scope", "Print inner in block and outer outside.", "block\nfunction",
                 "(let [outer \"function\"]\n  (let [inner \"block\"]\n    (println inner))\n  (println outer))"),
        Exercise(lv, "14-closure-counter", "Atom counter 1,2,3.", "1\n2\n3",
                 "(defn make-counter []\n  (let [n (atom 0)]\n    #(swap! n inc)))\n(let [c (make-counter)]\n  (println (c))\n  (println (c))\n  (println (c)))"),
    ]

    lv = "09-strings"
    exs += [
        Exercise(lv, "01-basics", 'GIVEN s = "JavaScript". Length, upper, lower.', "10\nJAVASCRIPT\njavascript",
                 '(require \'[clojure.string :as str])\n(let [s "JavaScript"]\n  (println (count s))\n  (println (str/upper-case s))\n  (println (str/lower-case s)))', given='(def s "JavaScript")'),
        Exercise(lv, "02-loop-chars", 'Print each char of "code".', "c\no\nd\ne",
                 '(let [s "code"]\n  (doseq [ch s] (println ch)))', given='(def s "code")'),
        Exercise(lv, "03-reverse", 'Reverse "bareilly" with loop.', "yllierab",
                 '(let [s "bareilly"]\n  (loop [chars (seq s) out ""]\n    (if (empty? chars) (println out)\n      (recur (rest chars) (str (first chars) out)))))', given='(def s "bareilly")'),
        Exercise(lv, "04-palindrome", "racecar palindrome.", "true",
                 '(let [s "racecar"]\n  (println (= s (apply str (reverse (seq s)))))', given='(def s "racecar")'),
        Exercise(lv, "05-count-vowels-consonants", "hello world counts.", "vowels: 3\nconsonants: 7",
                 '(require \'[clojure.string :as str])\n(let [s "hello world" letters (filter #(Character/isLetter %) s)]\n  (let [v (count (filter #(#{\\a \\e \\i \\o \\u} (Character/toLowerCase %)) letters))]\n    (println "vowels:" v)\n    (println "consonants:" (- (count letters) v))))', given='(def s "hello world")'),
        Exercise(lv, "06-word-count", "Word count with extra spaces.", "4",
                 '(require \'[clojure.string :as str])\n(let [s " the quick  brown fox "]\n  (println (count (str/split (str/trim s) #\\s+))))', given='(def s " the quick  brown fox ")'),
        Exercise(lv, "07-title-case", "Capitalise each word.", "Learning Javascript Today",
                 '(require \'[clojure.string :as str])\n(let [s "learning javascript today"]\n  (println (str/join " " (map str/capitalize (str/split s #\\s+)))))', given='(def s "learning javascript today")'),
        Exercise(lv, "08-remove-duplicates", "Remove duplicate chars.", "progamin",
                 '(let [s "programming"]\n  (println (apply str (reduce (fn [acc ch] (if (some #{ch} acc) acc (conj acc ch))) [] s))))', given='(def s "programming")'),
        Exercise(lv, "09-split-join", "Split and join.", "a - b - c - d",
                 '(require \'[clojure.string :as str])\n(let [s "a,b,c,d"]\n  (println (str/join " - " (str/split s #","))))', given='(def s "a,b,c,d")'),
        Exercise(lv, "10-search-methods", "includes/start/end/index.", "true\ntrue\nfalse\n1",
                 '(require \'[clojure.string :as str])\n(let [s "javascript"]\n  (println (str/includes? s "script"))\n  (println (str/starts-with? s "java"))\n  (println (str/ends-with? s "x"))\n  (println (str/index-of s "a")))', given='(def s "javascript")'),
        Exercise(lv, "11-slice", "subs drills cde/fgh/abc.", "cde\nfgh\nabc",
                 '(let [s "abcdefgh"]\n  (println (subs s 2 5))\n  (println (subs s (- (count s) 3)))\n  (println (subs s 2 5)))', given='(def s "abcdefgh")'),
        Exercise(lv, "12-replace", "replace first vs replace all.", "dog bat cat\ndog bat dog",
                 '(require \'[clojure.string :as str])\n(let [s "cat bat cat"]\n  (println (str/replace-first s "cat" "dog"))\n  (println (str/replace s "cat" "dog")))', given='(def s "cat bat cat")'),
        Exercise(lv, "13-trim-pad", "trim and pad.", "7\n00007",
                 '(require \'[clojure.string :as str])\n(let [s "  7  " t (str/trim s)]\n  (println t)\n  (println (format "%05d" (parse-long t))))', given='(def s "  7  ")'),
        Exercise(lv, "14-anagram", "listen/silent anagram.", "true",
                 '(let [a "listen" b "silent"]\n  (println (= (sort (seq a)) (sort (seq b)))))', given='(def a "listen")\n(def b "silent")'),
    ]

    lv = "10-vectors"
    exs += [
        Exercise(lv, "01-basics", "Length, first, last of vector.", "3\n10\n30",
                 "(let [arr [10 20 30]]\n  (println (count arr))\n  (println (first arr))\n  (println (last arr)))", given="(def arr [10 20 30])"),
        Exercise(lv, "02-mutate", "conj/pop/peek immutable style.", "1 2 3 4\n2 3",
                 "(let [arr [2 3]\n      a (conj (conj arr 4) 1)\n      b (pop (pop a))]\n  (println (clojure.string/join \" \" a))\n  (println (clojure.string/join \" \" b)))", given="(def arr [2 3])"),
        Exercise(lv, "03-two-loops", "doseq twice.", "a\nb\nc\na\nb\nc",
                 "(let [arr [\"a\" \"b\" \"c\"]]\n  (doseq [x arr] (println x))\n  (doseq [x arr] (println x)))", given='(def arr ["a" "b" "c"])'),
        Exercise(lv, "04-sum-average", "Sum and average.", "108\n18.00",
                 "(let [arr [4 8 15 16 23 42] sum (reduce + arr)]\n  (println sum)\n  (println (format \"%.2f\" (/ sum (count arr)))))", given="(def arr [4 8 15 16 23 42])"),
        Exercise(lv, "05-largest", "Largest without max.", "41",
                 "(let [arr [3 41 7 41 19]]\n  (println (reduce (fn [acc x] (if (> x acc) x acc)) arr)))", given="(def arr [3 41 7 41 19])"),
        Exercise(lv, "06-second-largest", "Second distinct largest.", "34",
                 "(let [arr [12 35 1 10 34 35] sorted (sort > (distinct arr))]\n  (println (second sorted)))", given="(def arr [12 35 1 10 34 35])"),
        Exercise(lv, "07-is-sorted", "Non-decreasing check.", "true",
                 "(let [arr [1 2 2 5 9]]\n  (println (every? true? (map >= (rest arr) arr))))", given="(def arr [1 2 2 5 9])"),
        Exercise(lv, "08-reverse-in-place", "Reverse with loop into new vector.", "5 4 3 2 1",
                 "(let [arr [1 2 3 4 5]\n      rev (loop [i (dec (count arr)) acc []]\n        (if (neg? i) acc (recur (dec i) (conj acc (arr i)))))]\n  (println (clojure.string/join \" \" rev)))", given="(def arr [1 2 3 4 5])"),
        Exercise(lv, "09-linear-search", "Index of 9.", "2",
                 "(let [arr [7 3 9 1] target 9]\n  (println (first (keep-indexed #(when (= %2 target) %1) arr))))", given="(def arr [7 3 9 1])\n(def target 9)"),
        Exercise(lv, "10-count-occurrences", "Count 3s.", "3",
                 "(let [arr [1 3 3 5 3] target 3]\n  (println (count (filter #{target} arr))))", given="(def arr [1 3 3 5 3])\n(def target 3)"),
        Exercise(lv, "11-remove-duplicates-sorted", "Unique sorted.", "1 2 3",
                 "(let [arr [1 1 2 2 2 3 3]]\n  (println (clojure.string/join \" \" (distinct arr))))", given="(def arr [1 1 2 2 2 3 3])"),
        Exercise(lv, "12-rotate-one", "Left rotate 1.", "2 3 4 5 1",
                 "(let [arr [1 2 3 4 5] n (count arr)]\n  (println (clojure.string/join \" \" (concat (subvec arr 1 n) [(arr 0)]))))", given="(def arr [1 2 3 4 5])"),
        Exercise(lv, "13-rotate-k", "Rotate k=3.", "4 5 6 7 1 2 3",
                 "(let [arr [1 2 3 4 5 6 7] k 3 n (count arr) k (mod k n)]\n  (println (clojure.string/join \" \" (concat (subvec arr k n) (subvec arr 0 k)))))", given="(def arr [1 2 3 4 5 6 7])\n(def k 3)"),
        Exercise(lv, "14-move-zeros", "Move zeros end.", "1 3 12 0 0",
                 "(let [arr [0 1 0 3 12]]\n  (println (clojure.string/join \" \" (concat (remove zero? arr) (repeat (count (filter zero? arr)) 0)))))", given="(def arr [0 1 0 3 12])"),
        Exercise(lv, "15-union-sorted", "Sorted union.", "1 2 3 4 5 6",
                 "(let [a [1 2 3 4 6] b [2 3 5]]\n  (println (clojure.string/join \" \" (sort (set (concat a b))))))", given="(def a [1 2 3 4 6])\n(def b [2 3 5])"),
        Exercise(lv, "16-missing-number", "Missing 0..n.", "3",
                 "(let [arr [0 1 2 4 5] n 5 expected (* n (+ n 1) (/ 1 2))]\n  (println (- expected (reduce + arr))))", given="(def arr [0 1 2 4 5])\n(def n 5)"),
    ]

    lv = "11-seq-transforms"
    exs += [
        Exercise(lv, "01-foreach", "Print index: value with map-indexed.", "0: 10\n1: 20\n2: 30",
                 "(let [arr [10 20 30]]\n  (doseq [[i v] (map-indexed vector arr)] (println (str i \": \" v))))", given="(def arr [10 20 30])"),
        Exercise(lv, "02-map", "Doubled joined.", "2 4 6 8",
                 "(let [arr [1 2 3 4]]\n  (println (clojure.string/join \" \" (map #(* 2 %) arr))))", given="(def arr [1 2 3 4])"),
        Exercise(lv, "03-filter", "Evens joined.", "2 4 6 8 10",
                 "(let [arr (range 1 11)]\n  (println (clojure.string/join \" \" (filter even? arr))))", given="(def arr (range 1 11))"),
        Exercise(lv, "04-reduce-sum", "Reduce sum.", "30",
                 "(let [arr [5 10 15]]\n  (println (reduce + arr)))", given="(def arr [5 10 15])"),
        Exercise(lv, "05-reduce-max", "Reduce max.", "19",
                 "(let [arr [4 19 7 2]]\n  (println (reduce max arr)))", given="(def arr [4 19 7 2])"),
        Exercise(lv, "06-find", "First >7 and index.", "8\n1",
                 "(let [arr [3 8 12 5]]\n  (println (first (filter #(> % 7) arr)))\n  (println (first (keep-indexed #(when (> %2 7) %1) arr))))", given="(def arr [3 8 12 5])"),
        Exercise(lv, "07-some-every", "some odd, every even.", "true\nfalse",
                 "(let [arr [2 4 6 7]]\n  (println (some odd? arr))\n  (println (every? even? arr)))", given="(def arr [2 4 6 7])"),
        Exercise(lv, "08-sort-numbers", "Sort asc/desc.", "2 9 10 100\n100 10 9 2",
                 "(let [arr [10 9 100 2]]\n  (println (clojure.string/join \" \" (sort arr)))\n  (println (clojure.string/join \" \" (sort > arr))))", given="(def arr [10 9 100 2])"),
        Exercise(lv, "09-sort-strings", "Sort strings.", "apple banana cherry",
                 '(let [arr ["banana" "apple" "cherry"]]\n  (println (clojure.string/join " " (sort arr)))', given='(def arr ["banana" "apple" "cherry"])'),
        Exercise(lv, "10-chaining", "Evens squared sum.", "220",
                 "(->> (range 1 11) (filter even?) (map #(* % %)) (reduce +) println)", given="(def arr (range 1 11))"),
        Exercise(lv, "11-flat", "Flatten one level vs full.", "1 2 3 4 5\n1 2 3 4 5",
                 "(let [arr [1 [2 3] [4 [5]]]]\n  (println (clojure.string/join \" \" (flatten arr)))\n  (println (clojure.string/join \" \" (clojure.core/flatten arr))))", given="(def arr [1 [2 3] [4 [5]]])"),
        Exercise(lv, "12-immutability", "map returns new vector.", "2 4 6\n1 2 3",
                 "(let [arr [1 2 3] mapped (map #(* 2 %) arr)]\n  (println (clojure.string/join \" \" mapped))\n  (println (clojure.string/join \" \" arr)))", given="(def arr [1 2 3])"),
    ]

    lv = "12-maps"
    exs += [
        Exercise(lv, "01-access", "Keyword and bracket access.", "Ada\n36",
                 '(let [user {:name "Ada" :age 36}]\n  (println (:name user))\n  (println (get user :age)))', given='(def user {:name "Ada" :age 36})'),
        Exercise(lv, "02-modify", "Assoc/dissoc — print keys.", "name city",
                 '(let [user (-> {:name "Ada" :age 36}\n                 (assoc :city "London")\n                 (update :age inc)\n                 (dissoc :age))]\n  (println (clojure.string/join " " (sort (keys user)))))', given='(def user {:name "Ada" :age 36})'),
        Exercise(lv, "03-for-in", "doseq keys.", "math: 90\nscience: 85\nart: 72",
                 '(let [scores {:math 90 :science 85 :art 72}]\n  (doseq [[k v] scores] (println (str (name k) ": " v))))', given="(def scores {:math 90 :science 85 :art 72})"),
        Exercise(lv, "04-keys-values-entries", "keys values count.", "math science art\n90 85 72\n3",
                 '(let [scores {:math 90 :science 85 :art 72}]\n  (println (clojure.string/join " " (map name (keys scores))))\n  (println (clojure.string/join " " (vals scores)))\n  (println (count scores)))', given="(def scores {:math 90 :science 85 :art 72})"),
        Exercise(lv, "05-nested", "Nested city.", "Bareilly",
                 '(let [user {:address {:city "Bareilly"}}]\n  (println (get-in user [:address :city])))', given='(def user {:address {:city "Bareilly"}})'),
        Exercise(lv, "06-list-names", "People names lines.", "Ada\nRaman\nMeera",
                 f"(let [people {PEOPLE}]\n  (doseq [p people] (println (:name p))))", given=f"(def people {PEOPLE})"),
        Exercise(lv, "07-filter-objects", "Names over 30.", "Ada, Raman",
                 f"(let [people {PEOPLE}]\n  (println (clojure.string/join \", \" (map :name (filter #(> (:age %) 30) people)))))", given=f"(def people {PEOPLE})"),
        Exercise(lv, "08-sort-objects", "Sort by age names.", "Meera Ada Raman",
                 f"(let [people {PEOPLE}]\n  (println (clojure.string/join \" \" (map :name (sort-by :age people)))))", given=f"(def people {PEOPLE})"),
        Exercise(lv, "09-destructure", "Destructure map.", "Ada — London",
                 '(let [user {:name "Ada" :age 36 :city "London"}\n      {:keys [name city]} user]\n  (println name "—" city))', given='(def user {:name "Ada" :age 36 :city "London"})'),
        Exercise(lv, "10-spread-merge", "merge maps.", "light\n18",
                 '(let [defaults {:theme "light" :font-size 14}\n      custom {:font-size 18}\n      merged (merge defaults custom)]\n  (println (:theme merged))\n  (println (:font-size merged)))', given="(def defaults {:theme \"light\" :font-size 14})\n(def custom {:font-size 18})"),
        Exercise(lv, "11-json", "Cheshire JSON round-trip.", '{"name":"Ada","age":36,"city":"London"}\nAda',
                 '(require \'[cheshire.core :as json])\n(let [people [{:name "Ada" :age 36 :city "London"}]\n      s (json/generate-string (first people))\n      parsed (json/parse-string s true)]\n  (println s)\n  (println (:name parsed)))',
                 given=f"(def people {PEOPLE})"),
        Exercise(lv, "12-optional-chaining", "get-in and default.", "nil\nunknown",
                 '(let [user {:name "Ada"}]\n  (println (get-in user [:address :city]))\n  (println (or (get-in user [:address :city]) "unknown")))', given='(def user {:name "Ada"})'),
    ]

    lv = "13-recursion"
    exs += [
        Exercise(lv, "01-print-n-times", "Print learning 4 times recursively.", "learning\nlearning\nlearning\nlearning",
                 "(defn print-times [n]\n  (when (pos? n)\n    (println \"learning\")\n    (print-times (dec n))))\n(print-times 4)"),
        Exercise(lv, "02-print-one-to-n", "Print 1..5 recursively.", "1\n2\n3\n4\n5",
                 "(defn print-1-to [n]\n  (when (<= 1 n)\n    (print-1-to (dec n))\n    (println n)))\n(print-1-to 5)", given="(def n 5)"),
        Exercise(lv, "03-print-n-to-one", "Print 5..1 recursively.", "5\n4\n3\n2\n1",
                 "(defn print-down [n]\n  (when (pos? n)\n    (println n)\n    (print-down (dec n))))\n(print-down 5)", given="(def n 5)"),
        Exercise(lv, "04-sum-to-n", "sum-to recursively.", "tests",
                 "(defn sum-to [n]\n  (if (<= n 1) n (+ n (sum-to (dec n)))))",
                 fn_stub=("sum-to", "[n]", "0"), test_body="(deftest sum-to-test\n  (is (= (sum-to 5) 15))\n  (is (= (sum-to 1) 1)))"),
        Exercise(lv, "05-factorial", "factorial recursively.", "tests",
                 "(defn factorial [n]\n  (if (<= n 1) 1 (* n (factorial (dec n)))))",
                 fn_stub=("factorial", "[n]", "0"), test_body="(deftest factorial-test\n  (is (= (factorial 5) 120))\n  (is (= (factorial 0) 1)))"),
        Exercise(lv, "06-reverse-array", "reverse vector recursively.", "tests",
                 "(defn reverse-array [v]\n  (loop [i (dec (count v)) acc []]\n    (if (neg? i) acc (recur (dec i) (conj acc (v i))))))",
                 fn_stub=("reverse-array", "[v]", "[]"), test_body='(deftest reverse-test\n  (is (= (reverse-array ["a" "b" "c"]) ["c" "b" "a"])))'),
        Exercise(lv, "07-is-palindrome", "palindrome string recursive indices.", "tests",
                 "(defn is-palindrome [s]\n  (let [n (count s)]\n    (loop [i 0 j (dec n)]\n      (if (>= i j) true\n        (if (= (nth s i) (nth s j)) (recur (inc i) (dec j)) false)))))",
                 fn_stub=("is-palindrome", "[s]", "false"), test_body='(deftest pal-test\n  (is (is-palindrome "racecar"))\n  (is (not (is-palindrome "abc"))))'),
        Exercise(lv, "08-fibonacci", "fib n recursively.", "tests",
                 "(defn fib [n]\n  (cond (= n 0) 0 (= n 1) 1 :else (+ (fib (dec n)) (fib (- n 2)))))",
                 fn_stub=("fib", "[n]", "0"), test_body="(deftest fib-test\n  (is (= (fib 0) 0))\n  (is (= (fib 6) 8)))"),
        Exercise(lv, "09-power", "power recursively.", "tests",
                 "(defn power [base exp]\n  (if (zero? exp) 1 (* base (power base (dec exp)))))",
                 fn_stub=("power", "[base exp]", "0"), test_body="(deftest power-test\n  (is (= (power 2 10) 1024)))"),
        Exercise(lv, "10-sum-digits", "sum digits recursively.", "tests",
                 "(defn sum-digits [n]\n  (if (zero? n) 0 (+ (rem n 10) (sum-digits (quot n 10)))))",
                 fn_stub=("sum-digits", "[n]", "0"), test_body="(deftest sum-digits-test\n  (is (= (sum-digits 123) 6)))"),
    ]

    lv = "14-frequency"
    exs += [
        Exercise(lv, "01-char-count-object", "Freq map banana.", "b:1 a:3 n:2",
                 '(let [s "banana" freqs (reduce (fn [m ch] (update m ch (fnil inc 0))) {} s) order (distinct s)]\n  (println (clojure.string/join " " (map #(str % ":" (freqs %)) order))))', given='(def s "banana")'),
        Exercise(lv, "02-char-count-map", "Same with frequencies.", "b:1 a:3 n:2",
                 '(let [s "banana" f (frequencies s) order (distinct s)]\n  (println (clojure.string/join " " (map #(str % ":" (f %)) order))))', given='(def s "banana")'),
        Exercise(lv, "03-array-frequency", "Array freq insertion order.", "10:3 5:2 15:1",
                 "(let [arr [10 5 10 15 10 5] freqs (frequencies arr) order (distinct arr)]\n  (println (clojure.string/join \" \" (map #(str % \":\" (freqs %)) order))))",
                 given="(def arr [10 5 10 15 10 5])"),
        Exercise(lv, "04-high-low-frequency", "Highest/lowest freq.", "highest: 10\nlowest: 15",
                 "(let [arr [10 5 10 15 10 5] freqs (frequencies arr)]\n  (let [[hi _] (apply max-key val freqs)\n        [lo _] (apply min-key val freqs)]\n    (println \"highest:\" hi)\n    (println \"lowest:\" lo)))", given="(def arr [10 5 10 15 10 5])"),
        Exercise(lv, "05-set-unique", "Unique values.", "1 2 3\n3",
                 "(let [arr [1 2 2 3 3 3] u (sort (set arr))]\n  (println (clojure.string/join \" \" u))\n  (println (count u)))", given="(def arr [1 2 2 3 3 3])"),
        Exercise(lv, "06-set-operations", "Union and intersection.", "1 2 3 4 5\n3 4",
                 "(require '[clojure.set :as set])\n(let [a [1 2 3 4] b [3 4 5]]\n  (println (clojure.string/join \" \" (sort (set/union a b))))\n  (println (clojure.string/join \" \" (sort (set/intersection a b)))))",
                 given="(def a [1 2 3 4])\n(def b [3 4 5])"),
        Exercise(lv, "07-first-non-repeating", "First unique char.", "w",
                 '(let [s "swiss" freqs (frequencies s)]\n  (println (or (first (filter #(= 1 (freqs %)) s)) "none")))', given='(def s "swiss")'),
        Exercise(lv, "08-two-sum", "Two sum indices.", "0 1",
                 "(let [arr [2 7 11 15] target 9 seen {}]\n  (loop [i 0 m {}]\n    (if (= i (count arr)) nil\n      (let [x (nth arr i) need (- target x)]\n        (if (contains? m need) (do (println (str (get m need) \" \" i)) nil)\n          (recur (inc i) (assoc m x i)))))))",
                 given="(def arr [2 7 11 15])\n(def target 9)"),
        Exercise(lv, "09-group-by-letter", "Group words by first letter.", "a: apple, avocado\nb: banana, blueberry\nc: cherry",
                 '(let [words ["apple" "avocado" "banana" "blueberry" "cherry"]\n      groups (group-by #(first %) words)]\n  (doseq [k (sort groups)]\n    (println (str k ": " (clojure.string/join ", " (groups k))))))',
                 given='(def words ["apple" "avocado" "banana" "blueberry" "cherry"])'),
        Exercise(lv, "10-anagram-map", "Anagram via freq.", "true",
                 '(let [a "anagram" b "nagaram"]\n  (println (= (frequencies a) (frequencies b))))', given='(def a "anagram")\n(def b "nagaram")'),
    ]

    lv = "15-namespaces-effects"
    exs += [
        Exercise(
            lv,
            "01-default-export",
            "Require helpers.greet and print Hello, Ada!",
            "Hello, Ada!",
            '(require \'helpers.greet)\n(println (helpers.greet/greet "Ada"))',
            extra_solution_files={
                "helpers/greet.clj": textwrap.dedent(
                    """
                    (ns helpers.greet)
                    (defn greet [name]
                      (str "Hello, " name "!"))
                    """
                ).strip(),
            },
        ),
        Exercise(
            lv,
            "02-named-exports",
            "Require helpers.math add and subtract.",
            "8\n2",
            '(require \'[helpers.math :as m])\n(println (m/add 5 3))\n(println (m/subtract 5 3))',
            extra_solution_files={
                "helpers/math.clj": textwrap.dedent(
                    """
                    (ns helpers.math)
                    (defn add [a b] (+ a b))
                    (defn subtract [a b] (- a b))
                    """
                ).strip(),
            },
        ),
        Exercise(lv, "03-try-catch", "Parse invalid edn/json safely.", "caught an error\nstill running",
                 '(try\n  (read-string "not json")\n  (catch Exception _\n    (println "caught an error")))\n(println "still running")'),
        Exercise(lv, "04-throw", "divide throws on zero.", "Cannot divide by zero",
                 '(defn divide [a b]\n  (when (zero? b)\n    (throw (ex-info "Cannot divide by zero" {})))\n  (/ a b))\n(try\n  (divide 10 0)\n  (catch Exception e\n    (println (.getMessage e))))'),
        Exercise(lv, "05-finally", "try/catch/finally demo.", "try ok\nfinally\ncaught\nfinally",
                 '(try\n  (try\n    (println "try ok")\n    (throw (ex-info "fail" {}))\n    (finally (println "finally")))\n  (catch Exception _\n    (println "caught"))\n  (finally (println "finally")))'),
        Exercise(lv, "06-settimeout-order", "future/delay ordering.", "first\nsecond\nthird",
                 '(println "first")\n(def f (future (println "third")))\n(println "second")\n@f'),
        Exercise(lv, "07-callback-style", "Callback with future.", "Ada",
                 '(defn get-user [id cb]\n  (future (cb {:id id :name "Ada"})))\n(get-user 1 #(println (:name %)))\n(Thread/sleep 20)'),
        Exercise(lv, "08-promise", "promise deliver.", "done",
                 '(let [p (promise)]\n  (future (deliver p "done"))\n  (println @p))'),
        Exercise(lv, "09-promise-reject", "Handle exception from future.", "failed",
                 '(let [p (promise)]\n  (future (deliver p (throw (ex-info "failed" {}))))\n  (try (println @p) (catch Exception e (println (.getMessage e)))))'),
        Exercise(lv, "10-async-await", "delay/deref async style.", "done",
                 '(let [d (delay (do (Thread/sleep 10) "done"))]\n  (println @d))'),
        Exercise(lv, "11-promise-all", "Multiple futures joined.", "1 2 3",
                 '(let [f1 (future (do (Thread/sleep 5) 1))\n      f2 (future (do (Thread/sleep 10) 2))\n      f3 (future (do (Thread/sleep 15) 3))]\n  (println (clojure.string/join " " [@f1 @f2 @f3])))'),
        Exercise(lv, "12-read-file", "slurp sample.txt.", "hello from a file",
                 '(println (clojure.string/trim (slurp "levels/15-namespaces-effects/data/sample.txt")))'),
    ]

    return exs
