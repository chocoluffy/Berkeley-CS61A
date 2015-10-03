## Object-Oriented Programming ##

# Q2
class Person(object):
    """Person class.

    >>> steven = Person("Steven")
    >>> steven.repeat()       # starts at whatever value you'd like
    'I squirreled it away before it could catch on fire.'
    >>> steven.say("Hello")
    'Hello'
    >>> steven.repeat()
    'Hello'
    >>> steven.greet()
    'Hello, my name is Steven'
    >>> steven.repeat()
    'Hello, my name is Steven'
    >>> steven.ask("preserve abstraction barriers")
    'Would you please preserve abstraction barriers'
    >>> steven.repeat()
    'Would you please preserve abstraction barriers'
    """
    def __init__(self, name):
        self.name = name
        self.content=''
        "*** YOUR CODE HERE ***"

    def say(self, stuff):
        "*** YOUR CODE HERE ***"
        self.content=stuff
        return stuff

    def ask(self, stuff):
        return self.say("Would you please " + stuff)

    def greet(self):
        return self.say("Hello, my name is " + self.name)

    def repeat(self):
        if self.content=='':
            return 'I squirreled it away before it could catch on fire.'
        else:
            return self.content
        "*** YOUR CODE HERE ***"

# Q3
class Account(object):
    """A bank account that allows deposits and withdrawals.

    >>> eric_account = Account('Eric')
    >>> eric_account.deposit(1000000)   # depositing my paycheck for the week
    1000000
    >>> eric_account.transactions
    [('deposit', 1000000)]
    >>> eric_account.withdraw(100)      # buying dinner
    999900
    >>> eric_account.transactions
    [('deposit', 1000000), ('withdraw', 100)]
    """

    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions=[]
        "*** YOUR CODE HERE ***"

    def deposit(self, amount):
        """Increase the account balance by amount and return the
        new balance.
        """
        "*** YOUR CODE HERE ***"
        self.balance = self.balance + amount
        self.transactions+=[('deposit', amount)]
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance.
        """
        "*** YOUR CODE HERE ***"
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        self.transactions+=[('withdraw', amount)]
        return self.balance




# Q4
class BadBankAccount(Account):
    """ A subclass of bank account that allows an account holder to overdraw
    once, and then prevents them from withdrawing more money. You should also
    implement the property method overdrawn, which allows an account holder to
    check if they are overdrawn.

    >>> harold_account = BadBankAccount('Harold')
    >>> harold_account.deposit(100)   # depositing my paycheck for the week
    100
    >>> harold_account.withdraw(101)  # buying dinner
    -1
    >>> harold_account.overdrawn
    True
    >>> harold_account.withdraw(100000)
    You have overdrawn, please add more money!
    -1
    >>> harold_account.deposit(10)
    9
    >>> harold_account.overdrawn
    False
    """

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance.
        """
        "*** YOUR CODE HERE ***"
        if self.balance<0:
            print("You have overdrawn, please add more money!") 
            return self.balance
        else:
            self.balance = self.balance - amount
            return self.balance

    "*** YOUR CODE HERE ***"
    @property
    def overdrawn(self):
        if self.balance<0:
            return True
        else:
            return False


