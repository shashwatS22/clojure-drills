(ns runner.hints)

(def ^:private hints
  {"04-for-loops/12-fibonacci" "Check your loop's starting values."
   "06-patterns/09-pyramid" "Build each row as one string, then println once."
   "13-recursion/05-factorial" "Base case: n is 0 or 1. Use recur for the recursive step."})

(defn all [] hints)
