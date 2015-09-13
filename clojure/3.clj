(defn find-first [f coll]
  (first 
    (filter f coll)))

(defn from-sqrt [x] 
  (iterate inc 
    (int (Math/sqrt x))))

(defn factor? [x y]
  (zero? (mod x y)))

(defn find-factor [x]
  (let [m (find-first (partial factor? x)
            (from-sqrt x))]
       (if (= m 1) x m)))

(defn prime-factors
  [x] 
    (let [m (find-factor x)
        n (/ x m)]
    (if (= n 1)
      [m]
      (concat (prime-factors m) 
              (prime-factors n)))))

(defn largest-prime-factor
  [x]
  (apply max (prime-factors x)))

(println (largest-prime-factor 600851475143))
