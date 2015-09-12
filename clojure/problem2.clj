(defn fib-step [[a b]] 
  [b (+ a b)])

(println (reduce + 
  (filter even? 
    (take-while (partial > 4000000) 
      (map first 
        (iterate fib-step [1 1]))))))
