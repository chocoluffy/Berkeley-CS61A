def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 3
    else:
        return g(n-1)+2*g(n-2)+3*g(n-3)


def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 3
    else:

        i=4
        one=1
        two=2
        three=3
        while(i<n+1):
            next=one*3+two*2+three
            one=two
            two=three
            three=next
            i+=1
        return next


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"
    if k<10:
        if k==7:
            return True
        else: return False
    else:
        if k%10==7:
            return True
        else:
            return has_seven(k//10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** YOUR CODE HERE ***"
    """count the turn. if count%2==0, increment
                       if count%2==1, decrement
        how to calaulate the count:
        if n%7==0 or contain_7(n)
        def contain_7():
            if n%10==7
                return true
            else: return contain_7(n//10)"""
    i=1
    count=0
    while i<n:
        if i%7==0:
            count+=1
        elif contain_7(i):
            count+=1
        i+=1
    
    if n<8:
        return n
    return pingpong(n-1)+pow(-1,count)
        
                       
def contain_7(n):
    if n%10==7:
        return True
    elif n<10:
        return False
    else: return contain_7(n//10)

from functools import lru_cache

@lru_cache(maxsize=None)
def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    def part(n,m):
        if n==0:
            return 1
        elif n<0:
            return 0
        elif m==0:
            return 0
        else: return part(n-m,num(m))+part(n,m//2)
    return part(amount, num(amount))



def num(n):
    i=0
    while i<n:
        if pow(2,i)==n:
            return pow(2,i)
        if pow(2,i)<n and pow(2,i+1)>n:
            return pow(2,i)
        else: i+=1


def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    if n==1:
        print("Move the top disk from rod",start,"to rod",end)
    else:
        towers_of_hanoi(n-1,start,other(start,end))
        towers_of_hanoi(1,start,end)
        towers_of_hanoi(n-1,other(start,end),end)

def other(x,y):
    if x+y==3:
        return 3
    elif x+y==4:
        return 2
    else:
        return 1


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return 'YOUR_EXPRESSION_HERE'
