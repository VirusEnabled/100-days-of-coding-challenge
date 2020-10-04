import numpy as np

"""
Euler Problem #3:

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

"""

def find_smallest_prime_factor(number):
	upper_bound = int(np.sqrt(number)) + 1

	for i in range(2, upper_bound):
		if number % i == 0:
			return i

	return number


def find_largest_prime_factor():
	number = 600851475143
	while True:
		smallest_factor = find_smallest_prime_factor(number)

		if smallest_factor < number:
			number //= smallest_factor
		else:
			return number


if __name__ == '__main__':
	result = find_largest_prime_factor()
	print(result)
