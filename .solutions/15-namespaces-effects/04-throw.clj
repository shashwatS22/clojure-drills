(defn divide [a b]
  (when (zero? b)
    (throw (ex-info "Cannot divide by zero" {})))
  (/ a b))
(try
  (divide 10 0)
  (catch Exception e
    (println (.getMessage e))))
