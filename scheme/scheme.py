"""A Scheme interpreter and its read-eval-print loop."""

from scheme_primitives import *
from scheme_reader import *
from ucb import main, trace

##############
# Eval/Apply #
##############

def scheme_eval(expr, env, _=None): # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in environment ENV.

    >>> expr = read_line("(+ 2 2)")
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # Atoms
    assert expr is not None
    if scheme_symbolp(expr):
        return env.lookup(expr)
    elif self_evaluating(expr):
        return expr

    # Combinations
    if not scheme_listp(expr):
        raise SchemeError("malformed list: {0}".format(str(expr)))
    first, rest = expr.first, expr.second
    "*** YOUR CODE HERE ***"
    if scheme_symbolp(first) and first in SPECIAL_FORMS:
        result = SPECIAL_FORMS[first](rest, env)
    else:
        procedure = scheme_eval(first, env)
        args = rest.map(lambda operand: scheme_eval(operand, env))
        result = scheme_apply(procedure, args, env)
    return result

def self_evaluating(expr):
    """Return whether EXPR evaluates to itself."""
    return scheme_atomp(expr) or scheme_stringp(expr) or expr is okay

def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS in environment ENV."""
    if isinstance(procedure, PrimitiveProcedure):
        return apply_primitive(procedure, args, env)
    elif isinstance(procedure, UserDefinedProcedure):
        new_env = make_call_frame(procedure, args, env)
        return eval_all(procedure.body, new_env)
    else:
        raise SchemeError("cannot call: {0}".format(str(procedure)))

def eval_all(expressions, env):
    """Evaluate a Scheme list of EXPRESSIONS & return the value of the last."""
    "*** YOUR CODE HERE ***"
    n = 0
    if not expressions:
        return okay
    for expression in expressions:
        n += 1
        if n == len(expressions):
            return scheme_eval(expression, env, True)
        result = scheme_eval(expression, env)
    return result
   
def apply_primitive(procedure, args_scheme_list, env):
    """Apply PrimitiveProcedure PROCEDURE to ARGS_SCHEME_LIST in ENV.

    >>> env = create_global_frame()
    >>> plus = env.bindings["+"]
    >>> twos = Pair(2, Pair(2, nil))
    >>> apply_primitive(plus, twos, env)
    4
    """
    args = list(args_scheme_list) # Convert a Scheme list to a Python list
    "*** YOUR CODE HERE ***"
    if procedure.use_env:
        args.append(env)
    try:
        return procedure.fn(*args)
    except TypeError:
        raise SchemeError

def make_call_frame(procedure, args, env):
    """Make a frame that binds the formal parameters of PROCEDURE to ARGS."""
    "*** YOUR CODE HERE ***"
    if isinstance(procedure, LambdaProcedure):
        environment = env.make_child_frame(procedure.formals, args)
        environment.parent = procedure.env 
        return environment
    elif isinstance(procedure, MuProcedure):
        return env.make_child_frame(procedure.formals, args)

################
# Environments #
################

class Frame:
    """An environment frame binds Scheme symbols to Scheme values."""

    def __init__(self, parent):
        """An empty frame with a PARENT frame (which may be None)."""
        self.bindings = {}
        self.parent = parent

    def __repr__(self):
        if self.parent is None:
            return "<Global Frame>"
        else:
            s = sorted('{0}: {1}'.format(k,v) for k,v in self.bindings.items())
            return "<{{{0}}} -> {1}>".format(', '.join(s), repr(self.parent))

    def lookup(self, symbol):
        """Return the value bound to SYMBOL.  Errors if SYMBOL is not found."""
        "*** YOUR CODE HERE ***"
        
        if symbol in self.bindings:
            return self.bindings[symbol]
        elif self.parent == None:
            raise SchemeError("unknown identifier: {0}".format(symbol))
        else:
            return self.parent.lookup(symbol)  

    def make_child_frame(self, formals, vals):
        """Return a new local frame whose parent is SELF, in which the symbols
        in a Scheme list of formal parameters FORMALS are bound to the Scheme
        values in the Scheme list VALS. Raise an error if too many or too few
        vals are given.

        >>> env = create_global_frame()
        >>> formals, expressions = read_line("(a b c)"), read_line("(1 2 3)")
        >>> env.make_child_frame(formals, expressions)
        <{a: 1, b: 2, c: 3} -> <Global Frame>>
        """
        frame = Frame(self) # Create a new frame with self as the parent
        "*** YOUR CODE HERE ***"
        if len(formals) < len(vals):
            raise SchemeError("Too many arguments!")
        elif len(formals) > len(vals):
            raise SchemeError("Need more arguments!")
        else:
            for index in range(len(formals)):
                frame.define(formals[index], vals[index])
        return frame

    def define(self, symbol, value):
        """Define Scheme SYMBOL to have VALUE."""
        self.bindings[symbol] = value

class UserDefinedProcedure:
    """A procedure defined by an expression."""

class LambdaProcedure(UserDefinedProcedure):
    """A procedure defined by a lambda expression or a define form."""

    def __init__(self, formals, body, env):
        """A procedure with formal parameter list FORMALS (a Scheme list),
        a Scheme list of BODY expressions, and a parent environment that
        starts with Frame ENV.
        """
        self.formals = formals
        self.body = body
        self.env = env

    def __str__(self):
        return str(Pair("lambda", Pair(self.formals, self.body)))

    def __repr__(self):
        return "LambdaProcedure({!r}, {!r}, {!r})".format(
            self.formals, self.body, self.env)

#################
# Special forms #
#################

def do_define_form(expressions, env):
    """Evaluate a define form."""
    check_form(expressions, 2)
    target = expressions[0]
    if scheme_symbolp(target):
        check_form(expressions, 2, 2)
        "*** YOUR CODE HERE ***"
        operand = expressions.second.first
        if type(operand) == int:
            env.define(target, operand)
        else:
            value = scheme_eval(operand, env)
            env.define(target, value)
        return target
        
    elif isinstance(target, Pair) and scheme_symbolp(target.first):
        "*** YOUR CODE HERE ***"
        func_name = target.first
        parameter = target.second
        body = expressions.second
        expr = Pair(parameter, body)
        lambda_form = do_lambda_form(expr, env)
        env.define(func_name, lambda_form)
        return func_name
    else:
        bad = target.first if isinstance(target, Pair) else target
        raise SchemeError("Non-symbol: {}".format(bad))

def do_quote_form(expressions, env):
    """Evaluate a quote form."""
    check_form(expressions, 1, 1)
    "*** YOUR CODE HERE ***"
    return expressions[0]

def do_begin_form(expressions, env):
    """Evaluate begin form."""
    check_form(expressions, 1)
    return eval_all(expressions, env)

def do_lambda_form(expressions, env):
    """Evaluate a lambda form."""
    check_form(expressions, 2)
    formals = expressions.first
    check_formals(formals)
    "*** YOUR CODE HERE ***"
    return LambdaProcedure(formals, expressions.second, env)

def do_if_form(expressions, env):
    """Evaluate an if form."""
    check_form(expressions, 2, 3)
    "*** YOUR CODE HERE ***"
    
    boolean = scheme_eval(expressions.first, env)
    case = expressions.second

    if scheme_true(boolean):
        return scheme_eval(case.first, env, True)
    elif scheme_false(boolean):
        if case.second == nil:
            return okay
        return scheme_eval(case.second.first, env, True)

def do_and_form(expressions, env):
    """Evaluate a short-circuited and form."""
    "*** YOUR CODE HERE ***"
    if not expressions:
        return True
    n = 0
    for condition in expressions:
        n += 1
        if n == len(expressions):
            value = scheme_eval(condition, env, True)
        else:
            value = scheme_eval(condition, env)
        if scheme_false(value):
            return False
    return value

def do_or_form(expressions, env):
    """Evaluate a short-circuited or form."""
    "*** YOUR CODE HERE ***"
    if not expressions:
        return False
    n = 0
    for condition in expressions:
        n += 1
        if n == len(expressions):
            value = scheme_eval(condition, env, True)
        else:
            value = scheme_eval(condition, env)
        if scheme_true(value):
            return value
    return False

def do_cond_form(expressions, env):
    """Evaluate a cond form."""
    num_clauses = len(expressions)
    for i, clause in enumerate(expressions):
        check_form(clause, 1)
        if clause.first == "else":
            if i < num_clauses-1:
                raise SchemeError("else must be last")
            test = True
            if clause.second is nil:
                raise SchemeError("badly formed else clause")
        else:
            test = scheme_eval(clause.first, env)
        if scheme_true(test):
            "*** YOUR CODE HERE ***"
            if not clause.second:
                return test
            return eval_all(clause.second, env)
    return okay
    
def do_let_form(expressions, env):
    """Evaluate a let form."""
    check_form(expressions, 2)
    let_env = make_let_frame(expressions.first, env)
    return eval_all(expressions.second, let_env)

def make_let_frame(bindings, env):
    """Create a frame containing bindings from a let expression."""
    if not scheme_listp(bindings):
        raise SchemeError("bad bindings list in let form")
    "*** YOUR CODE HERE ***"
    try:
        formals_lst, values_lst = [], []
        for formal, value in bindings:
            value = scheme_eval(value, env)
            formals_lst.append(formal)
            values_lst.append(value)
        check_formals(formals_lst)
        return env.make_child_frame(formals_lst, values_lst)
    except ValueError:
        raise SchemeError("Too many operands!")
    
SPECIAL_FORMS = {
    "and": do_and_form,
    "begin": do_begin_form,
    "cond": do_cond_form,
    "define": do_define_form,
    "if": do_if_form,
    "lambda": do_lambda_form,
    "let": do_let_form,
    "or": do_or_form,
    "quote": do_quote_form,
}

# Utility methods for checking the structure of Scheme programs

def check_form(expr, min, max=float('inf')):
    """Check EXPR is a proper list whose length is at least MIN and no more than
    MAX (default: no maximum). Raises a SchemeError if this is not the case."""
    if not scheme_listp(expr):
        raise SchemeError("badly formed expression: " + str(expr))
    length = len(expr)
    if length < min:
        raise SchemeError("too few operands in form")
    elif length > max:
        raise SchemeError("too many operands in form")

def check_formals(formals):
    """Check that FORMALS is a valid parameter list, a Scheme list of symbols
    in which each symbol is distinct. Raise a SchemeError if the list of formals
    is not a well-formed list of symbols or if any symbol is repeated.

    >>> check_formals(read_line("(a b c)"))
    """
    "*** YOUR CODE HERE ***"
    for element in formals:
        num_of_times = 0
        if not scheme_symbolp(element):
            raise SchemeError("Bad parameters!")
        for elem in formals: #Checks for the number of appearances.
            if element == elem:
                num_of_times += 1
            if num_of_times == 2:
                raise SchemeError("Repeated parameters!")

#################
# Dynamic Scope #
#################

class MuProcedure(UserDefinedProcedure):
    """A procedure defined by a mu expression, which has dynamic scope.
     _________________
    < Scheme is cool! >
     -----------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||
    """

    def __init__(self, formals, body):
        """A procedure with formal parameter list FORMALS (a Scheme list) and a
        Scheme list of BODY expressions.
        """
        self.formals = formals
        self.body = body

    def __str__(self):
        return str(Pair("mu", Pair(self.formals, self.body)))

    def __repr__(self):
        return "MuProcedure({!r}, {!r})".format(self.formals, self.body)


def do_mu_form(expressions, env):
    """Evaluate a mu form."""
    check_form(expressions, 2)
    formals = expressions[0]
    check_formals(formals)
    "*** YOUR CODE HERE ***"
    return MuProcedure(formals, expressions.second)

SPECIAL_FORMS["mu"] = do_mu_form

##################
# Tail Recursion #
##################

class Evaluate:
    """An expression EXPR to be evaluated in environment ENV."""
    def __init__(self, expr, env):
        self.expr = expr
        self.env = env

def scheme_optimized_eval(expr, env, tail=False):
    """Evaluate Scheme expression EXPR in environment ENV."""
    # Evaluate Atoms
    assert expr is not None
    if scheme_symbolp(expr):
        return env.lookup(expr)
    elif self_evaluating(expr):
        return expr

    if tail:
        "*** YOUR CODE HERE ***"
        return Evaluate(expr, env)
    else:
        result = Evaluate(expr, env)

    while isinstance(result, Evaluate):
        expr, env = result.expr, result.env
        # All non-atomic expressions are lists (combinations)
        if not scheme_listp(expr):
            raise SchemeError("malformed list: {0}".format(str(expr)))
        first, rest = expr.first, expr.second
        if (scheme_symbolp(first) and first in SPECIAL_FORMS):
            result = SPECIAL_FORMS[first](rest, env)
        else:
            procedure = scheme_eval(first, env)
            args = rest.map(lambda operand: scheme_eval(operand, env))
            result = scheme_apply(procedure, args, env)
    return result

################################################################
# Uncomment the following line to apply tail call optimization #
################################################################
scheme_eval = scheme_optimized_eval


################
# Input/Output #
################

def read_eval_print_loop(next_line, env, interactive=False, quiet=False,
                         startup=False, load_files=()):
    """Read and evaluate input until an end of file or keyboard interrupt."""
    if startup:
        for filename in load_files:
            scheme_load(filename, True, env)
    while True:
        try:
            src = next_line()
            while src.more_on_line:
                expression = scheme_read(src)
                result = scheme_eval(expression, env)
                if not quiet and result is not None:
                    print(result)
        except (SchemeError, SyntaxError, ValueError, RuntimeError) as err:
            if (isinstance(err, RuntimeError) and
                'maximum recursion depth exceeded' not in getattr(err, 'args')[0]):
                raise
            elif isinstance(err, RuntimeError):
                print("Error: maximum recursion depth exceeded")
            else:
                print("Error:", err)
        except KeyboardInterrupt:  # <Control>-C
            if not startup:
                raise
            print()
            print("KeyboardInterrupt")
            if not interactive:
                return
        except EOFError:  # <Control>-D, etc.
            print()
            return

def scheme_load(*args):
    """Load a Scheme source file. ARGS should be of the form (SYM, ENV) or (SYM,
    QUIET, ENV). The file named SYM is loaded in environment ENV, with verbosity
    determined by QUIET (default true)."""
    if not (2 <= len(args) <= 3):
        expressions = args[:-1]
        raise SchemeError('"load" given incorrect number of arguments: '
                          '{0}'.format(len(expressions)))
    sym = args[0]
    quiet = args[1] if len(args) > 2 else True
    env = args[-1]
    if (scheme_stringp(sym)):
        sym = eval(sym)
    check_type(sym, scheme_symbolp, 0, "load")
    with scheme_open(sym) as infile:
        lines = infile.readlines()
    args = (lines, None) if quiet else (lines,)
    def next_line():
        return buffer_lines(*args)

    read_eval_print_loop(next_line, env, quiet=quiet)
    return okay

def scheme_open(filename):
    """If either FILENAME or FILENAME.scm is the name of a valid file,
    return a Python file opened to it. Otherwise, raise an error."""
    try:
        return open(filename)
    except IOError as exc:
        if filename.endswith('.scm'):
            raise SchemeError(str(exc))
    try:
        return open(filename + '.scm')
    except IOError as exc:
        raise SchemeError(str(exc))

def create_global_frame():
    """Initialize and return a single-frame environment with built-in names."""
    env = Frame(None)
    env.define("eval", PrimitiveProcedure(scheme_eval, True))
    env.define("apply", PrimitiveProcedure(scheme_apply, True))
    env.define("load", PrimitiveProcedure(scheme_load, True))
    add_primitives(env)
    return env

@main
def run(*argv):
    import argparse
    parser = argparse.ArgumentParser(description='CS 61A Scheme interpreter')
    parser.add_argument('-load', '-i', action='store_true',
                       help='run file interactively')
    parser.add_argument('file', nargs='?',
                        type=argparse.FileType('r'), default=None,
                        help='Scheme file to run')
    args = parser.parse_args()

    next_line = buffer_input
    interactive = True
    load_files = []

    if args.file is not None:
        if args.load:
            load_files.append(getattr(args.file, 'name'))
        else:
            lines = args.file.readlines()
            def next_line():
                return buffer_lines(lines)
            interactive = False

    read_eval_print_loop(next_line, create_global_frame(), startup=True,
                         interactive=interactive, load_files=load_files)
    tscheme_exitonclick()
