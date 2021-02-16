"""
Problem # 5:
2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?
"""

def divisible(number):
    """
    verifies if the given number is divisible by all numbers
    from 1 to 20
    :param number: int
    :return: bool
    """
    result = True
    for item in range(1,21):
        if number % item != 0:
            result = False
            break
    return result


def smallest_divisible_by_first_20():
    """
    calculates the smallest number
    divisible by the numbers 1 to 20 evenly
    :return: int
    """
    for x in range(2,1000000000):
        if divisible(x):
            return x

if __name__ == '__main__':
    print(smallest_divisible_by_first_20())
