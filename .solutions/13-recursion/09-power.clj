(defn power [base exp]
  (if (zero? exp) 1 (* base (power base (dec exp)))))
