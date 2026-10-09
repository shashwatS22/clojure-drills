(defn get-user [id cb]
  (future (cb {:id id :name "Ada"})))
(get-user 1 #(println (:name %)))
(Thread/sleep 20)
