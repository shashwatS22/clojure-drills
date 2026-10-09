# Level 07 — Number problems

## What you'll learn
- Digits, primes, divisors, GCD/LCM
- Boolean checks like palindrome and Armstrong numbers
- Frequency of digits

## Concepts

### Digit count
Divide by 10 until zero.

```clojure
(loop [n 946 c 0]
  (if (zero? n) (println c) (recur (quot n 10) (inc c))))
;; 3
```


### Prime check
Try divisors up to sqrt(n).

```clojure
(println (not (some #(zero? (rem 97 %)) (range 2 10))))
;; true
```


## Common mistakes
- Checking primality with a loop to `n` instead of `sqrt(n)`.
- Dropping leading zeros when reversing (700 → 7).

## Before you start
Type every example above into `playground/scratch.clj` and run it with Babashka. Change a number and predict what happens before you run it again.

## Exercises
Work through the numbered files in order. Save each file to check it with the watcher.
