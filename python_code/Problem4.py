"""
Euler Problem #4:




A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def is_palindrome(number):
    """
    verifies if the given
     number is a palindrome

    :param number: int
    :return: bool
    """
    comparison = f"{number}"
    side1, side2 = comparison[:len(comparison)//2], comparison[len(comparison)//2:]
    return True if side1 == "".join(reversed(side2)) else False

def largest_palindrome_product():
    return max(x * y for x in range(100,1000)
                for y in range(100,1000) if is_palindrome(x*y))


if __name__ == '__main__':
    result = largest_palindrome_product()
    resultx = is_palindrome(9009)
    print(result)
