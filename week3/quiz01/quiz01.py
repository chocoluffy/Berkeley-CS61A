# CS 61A Fall 2014
# Name:
# Login:

def harmonic(x, y):
    """Return the harmonic mean of x and y.

    >>> harmonic(2, 6)
    3.0
    >>> harmonic(1, 1)
    1.0
    >>> harmonic(2.5, 7.5)
    3.75


    """
    "*** YOUR CODE HERE ***"
    xre=1/x
    yre=1/y
    sum=xre+yre
    sumrec=1/sum
    print(2*sumrec)

from math import pi

def pi_fraction(gap):
    """Print the fraction within gap of pi that has the smallest denominator.

    >>> pi_fraction(0.01)
    22 / 7 = 3.142857142857143
    >>> pi_fraction(1)
    3 / 1 = 3.0
    >>> pi_fraction(1/8)
    13 / 4 = 3.25
    >>> pi_fraction(1e-6)
    355 / 113 = 3.1415929203539825


    """
    "*** YOUR CODE HERE ***"
    n=1
    while int(n*(pi+gap))-int(n*(pi-gap))<1:
        n=n+1
    denominator=n
    numerator=int(n*(pi-gap))+1
    print(numerator, '/', denominator, '=', numerator/denominator)

def nearest_two(x):
    """Return the power of two that is nearest to x.

    >>> nearest_two(8)    # 2 * 2 * 2 is 8
    8.0
    >>> nearest_two(11.5) # 11.5 is closer to 8 than 16
    8.0
    >>> nearest_two(14)   # 14 is closer to 16 than 8
    16.0
    >>> nearest_two(2015)
    2048.0
    >>> nearest_two(.1)
    0.125
    >>> nearest_two(0.75) # Tie between 1/2 and 1
    1.0
    >>> nearest_two(1.5)  # Tie between 1 and 2
    2.0


    """
    "*** YOUR CODE HERE ***"
    i=-3
    while(2**i<x):
        i=i+1
    lower=abs(2**(i-1)-x)
    upper=abs(2**i-x)
    if lower<upper:
        return float(2**(i-1))
    else: return float(2**i)
    
    


