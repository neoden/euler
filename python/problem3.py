# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

import math
import sys

def random_sqrt_factor(x):
    f = int(math.sqrt(x))
    while x % f != 0:
        f += 1
        if f == x:
            return x, 1
    return f, int(x / f)

i = 600851475143
# i = 12

factors = []
factors.append(random_sqrt_factor(i))

while True:
    prime_factors = 0
    factors_ = []
    for f in factors:
        if f[1] == 1 or f[0] == 1:
            prime_factors += 1
            factors_.append(f)
        else:
            factors_.append(random_sqrt_factor(f[0]))
            factors_.append(random_sqrt_factor(f[1]))
    factors = factors_
    if prime_factors == len(factors):
        break

print(max([max(f) for f in factors]))