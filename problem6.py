# https://projecteuler.net/problem=6
# 
# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers 
# and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers 
# and the square of the #sum.

import sys

def sum_of_1_to_n(n):
	return int((n * n + n) / 2)

def test_sum_of_1_to_n():
	assert(sum_of_1_to_n(3) == 6)
	assert(sum_of_1_to_n(5) == 15)

def sum_of_squares_1_to_n(n):
	return ((n * n * n) + (2 * n * n) - sum_of_1_to_n(n-1)) / 3

def main():
	sq = sum_of_1_to_n(100)
	a = sq * sq - sum_of_squares_1_to_n(100)
	print(a)

def test():
	test_sum_of_1_to_n()

if __name__ == '__main__':
	if len(sys.argv) == 2 and sys.argv[1] == 'test':
		test()
	else:
		main()