(defn is-multiple-of-3-or-5 [x]
  (or (zero? (mod x 3)) (zero? (mod x 5))))

(println (reduce + (filter is-multiple-of-3-or-5 (range 1 1000))))