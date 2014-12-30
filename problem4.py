# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

import math
import sys

POW10 = (1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000)

def n_digits(x):
	return int(math.log10(x)) + 1

def test_n_digits():
	assert(n_digits(1) == 1)
	assert(n_digits(1609090) == 7)


def nth_digit(x, n):
	return int(x / (POW10[n])) % 10

def test_nth_digit():
	assert(nth_digit(9, 0) == 9)
	assert(nth_digit(91, 1) == 9)
	assert(nth_digit(391, 1) == 9)


def is_palindrome(x):
	d = n_digits(x)
	n_match = int(d / 2)
	upper = 0
	for n, i in enumerate(reversed(range(d - n_match, d))):
		upper += nth_digit(x, i) * POW10[n]
	lower = x % POW10[n_match]
	return upper == lower

def test_is_palindrome():
	assert(is_palindrome(9009) == True)
	assert(is_palindrome(239847) == False)

palindromes = {}

def main():
	for i in reversed(range(100, 999)):
		for j in reversed(range(i, 999)):
			p = i * j
			if is_palindrome(p):
				palindromes[p]= (i, j)
	max_p = max(palindromes.keys())
	factors = palindromes[max_p]
	print(max_p, factors)

def test():
	test_n_digits()
	test_nth_digit()
	test_is_palindrome()

if __name__ == '__main__':
	if len(sys.argv) == 2 and sys.argv[1] == 'test':
		test()
	else:
		main()