"""
Euler Problem #1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

-Solution:
    what we need to do is to verify whether
     any number from 1 to 999 is a multiple of 3 or 5
    this is done by using the module(%) operator,
    as long as the operation returns 0,
    it means it's a multiple of the given number
"""


def sum_of_all_multiples_3_and_5():
    """
    looks for the all multiples of 3 and 5 then sums them
    :return: int
    """
    return sum(multiple for multiple in range(1000) if multiple % 3 == 0 or multiple % 5 == 0)



if __name__ == '__main__':
    result = sum_of_all_multiples_3_and_5()
    print(result)