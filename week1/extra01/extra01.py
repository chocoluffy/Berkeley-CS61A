##################################
# Newton's method (from lecture) #
##################################

def improve(update, close, guess=1, max_updates=100):
    """Iteratively improve guess with update until close(guess) is true."""
    k = 0
    while not close(guess) and k < max_updates:
        guess = update(guess)
        k = k + 1
    return guess

def approx_eq(x, y, tolerance=1e-15):
    """Whether x is within tolerance of y."""
    return abs(x - y) < tolerance

def find_zero(f, df):
    """Return a zero of the function f with derivative df."""
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def newton_update(f, df):
    """Return an update function for f with derivative df."""
    def update(x):
        return x - f(x) / df(x)
    return update

def nth_root_of_a(n, a):
    """Return the nth root of a.

    >>> nth_root_of_a(2, 64)
    8.0
    >>> nth_root_of_a(3, 64)
    4.0
    >>> nth_root_of_a(6, 64)
    2.0
    """
    return find_zero(lambda x: pow(x, n) - a, lambda x: n * pow(x, n-1))

def intersect(f, df, g, dg):
    """Return where f with derivative df intersects g with derivative dg.

    >>> parabola, line = lambda x: x*x - 2, lambda x: x + 10
    >>> dp, dl = lambda x: 2*x, lambda x: 1
    >>> intersect(parabola, dp, line, dl)
    4.0
    """
    "*** YOUR CODE HERE ***"
    return find_zero(lambda x: f(x)-g(x),lambda x: df(x)-dg(x))

X = lambda x, derive: 1 if derive else x
K = lambda k: lambda x, derive: 0 if derive else k

def quadratic(a, b, c):
    """Return a quadratic polynomial a*x*x + b*x + c.

    >>> q_and_dq = quadratic(1, 6, 8) # x*x + 6*x + 8
    >>> q_and_dq(1.0, False)  # value at 1
    15.0
    >>> q_and_dq(1.0, True)   # derivative at 1
    8.0
    >>> q_and_dq(-1.0, False) # value at -1
    3.0
    >>> q_and_dq(-1.0, True)  # derivative at -1
    4.0
    """
    A, B, C = K(a), K(b), K(c)
    AXX = mul_fns(A, mul_fns(X, X))
    BX = mul_fns(B, X)
    return add_fns(AXX, add_fns(BX, C))

def add_fns(f_and_df, g_and_dg):
    """Return the sum of two polynomials."""
    "*** YOUR CODE HERE ***"
    return lambda x,False: f_and_df(x,False)+g_and_dg(x,False)

def mul_fns(f_and_df, g_and_dg):
    """Return the product of two polynomials."""
    "*** YOUR CODE HERE ***"
    return  lambda x,False: f_and_df(x,False)*g_and_dg(x,False)

def poly_zero(f_and_df):
    """Return a zero of polynomial f_and_df, which returns:
        f(x)  for f_and_df(x, False)
        df(x) for f_and_df(x, True)

    >>> q = quadratic(1, 6, 8)
    >>> round(poly_zero(q), 5) # Round to 5 decimal places
    -2.0
    >>> round(poly_zero(quadratic(-1, -6, -9)), 5)
    -3.0
    """
    "*** YOUR CODE HERE ***"


