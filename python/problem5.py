# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def find_smallest_common_divisible(x):
	if x < 2 or int(x) != x:
		raise ValueError("argument must be an integer greater or equal to 2")
	s = 1
	for i in range(2, x+1):
		if s % i != 0:
			n = i
			for j in reversed(range(2, i)):
				if n % j == 0 and (s * (n / j)) % i == 0:
					n = int(n / j)
			s = s * n
	return s

print(find_smallest_common_divisible(10))
print(find_smallest_common_divisible(20))
