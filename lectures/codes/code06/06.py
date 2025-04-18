from math import floor, sqrt 

# recursive function
def countQ(x):
    if nobody_in_front_of(x):
        return 1
    y = person_in_front_of(x)
    return countQ(y) + 1

def odd(x):
    if x==0:
        return False
    return even(x-1)

def even(x):
    if x == 0:
        return True
    return odd(x-1)

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def fact_iter(n):
    total, k = 1, 1
    # total = (k-1)!
    while k <= n:
        total, k = total*k, k+1
    # total = (k-1)! and k = n+1    
    return total

def fact_iter2recur(n):
    # total = (k-1)!
    def auxiliary_fact(k, total):
        if k == n+1:
            return total
        else:
            auxiliary_fact(k+1, k*total)
    
    return auxiliary_fact(1, 1)

def cascade(n):
    if n <10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)


def example(n):
    a = [True for _ in range(n)]
    for i in range(2, floor(sqrt(n)) + 1):
        if a[i]:
            j = i ** 2
        while j < n:
            a[j] = False
            j += i
    for i, b in enumerate(a):
        if b and i > 1:
            print(i)

def fact(n):
    """
    >>> fact(0)
    1
    >>> fact(1)
    1
    >>> fact(3) # 3 * 2 * 1
    6
    >>> fact(5)
    120
    """
    if n == 0:
        return 1
    else:
        return fact(n - 1) * n




def count_up(n):
    """
    >>> count_up(1)
    1
    >>> count_up(2)
    1
    2
    >>> count_up(4)
    1
    2
    3
    4
    """
    # if n == 1:
    #     print(1)
    # else:
    #     count_up(n - 1)
    #     print(n)

    if n == 1:
        print(1)
    else:
        count_up(n - 1)
        print(n)
    



def sum_digits(n):
    """
    >>> sum_digits(9)
    9
    >>> sum_digits(19)
    10
    >>> sum_digits(2019)
    12
    """
    
    # if n < 10:
    #     return n
    # else:
    #     all_but_last, last = n // 10, n % 10
    #     return sum_digits(all_but_last) + last
    if n < 10:
        return n
    else:
        all_but_last, last = n //10, n % 10
        return sum_digits(all_but_last) + last
   
def count_part(n, m):
    if n < 0 or m <= 0:
        return 0
    if m == 1 or n == 0:
        return 1
    w_m = count_part(n-m, m)
    wo_m = count_part(n, m-1)
    return w_m + wo_m