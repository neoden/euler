# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def is_multiple_of_3_or_5(x):
	if x % 3 == 0 or x % 5 == 0:
		return True
	else:
		return False

s = 0

for i in range(1, 1000):
	if is_multiple_of_3_or_5(i):
		s += i

print(s)