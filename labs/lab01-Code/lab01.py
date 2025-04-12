
# ANSWER QUESTION q1

# ANSWER QUESTION q2

# ANSWER QUESTION q3

def both_odd(a, b):
    """Returns True if both a and b are odd numbers.

    >>> both_odd(-1, 1)
    True
    >>> both_odd(2, 1)
    False
    """
    return (a % 2 == 1) and (b % 2 == 1) # You can replace this line!


def factorial(n):
    """Return the factorial of a positive integer n.

    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def is_triangle(a, b, c):
    """Given three integers (may be nonpositive), judge whether the three
    integers can form the three sides of a triangle.

    >>> is_triangle(2, 1, 3)
    False
    >>> is_triangle(5, -3, 4)
    False
    >>> is_triangle(2, 2, 2)
    True
    """
    if min(a, b, c) <= 0 or a + b <= c or a + c <= b or b + c <= a:
        return False
    else:
        return True


def number_of_nine(n):
    """Return the number of 9 in each digit of a positive integer n.

    >>> number_of_nine(999)
    3
    >>> number_of_nine(9876543)
    1
    """
    count = 0

    while n > 0:
        if n % 10 == 9:
            count += 1
        n = n // 10
    return count


def min_digit(x):
    """Return the min digit of x.

    >>> min_digit(10)
    0
    >>> min_digit(4224)
    2
    >>> min_digit(1234567890)
    0
    >>> # make sure that you are using return rather than print
    >>> a = min_digit(123)
    >>> a
    1
    """

    min_d = 9
    while x > 0:
        d = x % 10
        if d < min_d:
            min_d = d
        x = x // 10
    return min_d
