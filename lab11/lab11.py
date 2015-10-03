#############
# Iterators #
#############

class IteratorRestart:
    """
    >>> i = IteratorRestart(2, 7)
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    6
    7
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        "*** YOUR CODE HERE ***"
        self.start=start-1
        self.line=self.start
        self.end=end
    def __next__(self):
        "*** YOUR CODE HERE ***"
        if self.start==self.end:
            self.start=self.line
            raise StopIteration
        else:
            self.start+=1
            return self.start

    def __iter__(self):
        "*** YOUR CODE HERE ***"
        return self

##############
# Generators #
##############

def generator():
    print("Starting here")
    i = 0
    while i < 6:
        print("Before yield")
        yield i
        print("After yield")
        i += 1

def countdown(n):
    """
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    i = n
    while i >= 0:
        yield i 
        i-=1

class Countdown:
    """
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, number):
        self.start=number
    def __iter__(self):
        while self.start>=0:
            yield self.start
            self.start-=1

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    i = n
    while i >=1:
        if i ==1:
            yield 1
            return 1
        if i %2==0:
            yield i 
            i =i//2
        else:
            yield i 
            i = 3*i +1








