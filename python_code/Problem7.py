"""
Problem #7:

By listing the first six prime numbers:
 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""


def prime_number_10001():
    """
    gets the 10001 prime number
    :return: int
    """
    counter = 0
    for n in range(1,100000):
        if n % 2!=0 and n % 1 == 0:
            if counter == 10001:
                return n
            counter+=1


if __name__ == '__main__':
    print(prime_number_10001())