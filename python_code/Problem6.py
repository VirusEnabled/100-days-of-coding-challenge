"""
Problem # 6:
Find the difference between the sum of the squares
of the first one hundred natural numbers and the square of the sum.
"""


def difference_between_sum_of_squares():
    """
    sums the square of the first
    100 natural numbers then squares the sums of those
    100 natural numbers returning the absolute differente of the operation
    :return: int
    """
    squared = 0
    summed = 0
    for x in range(1,101):
        squared += x**2
        summed += x
    return abs(squared - summed**2)


if __name__ == '__main__':
    print(difference_between_sum_of_squares())