def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    "*** YOUR CODE HERE ***"
    password_lst=[]
    def withdraw(num, string): 
        nonlocal password_lst
        if len(password_lst)>2:
            return_string='Your account is locked. Attempts: '+str(password_lst)
            return  return_string
        else:
            if string ==password:
                nonlocal balance
                if num>balance:
                    return 'Insufficient funds'
                else:
                    balance-=num
                    return balance 
            else:
                password_lst+=[string]
                return  'Incorrect password'
                
    return withdraw



def make_joint(withdraw, old_password, new_password):
    """

    """
    joint_lst=[old_password, new_password]
    if type(withdraw(0, old_password))==str:
        return 'Incorrect password'
    else:
        def joint_account(money_to_get, password):
            nonlocal joint_lst
            if type(withdraw(0, password))==int:
                joint_lst+=password
            if password in joint_lst:
                return withdraw(money_to_get, password)
            else:
                return withdraw(money_to_get, password)

    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"


    


    



class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, item, price_of_candy):
        self.product=item
        self.num_of_product=0
        self.product_price=price_of_candy
        self.balance=0
    def vend(self):
        if self.num_of_product<1:
            return 'Machine is out of stock.'
        elif self.balance<self.product_price:
            output='You must deposit $'+str(self.product_price-self.balance)+' more.'
            return output
        elif self.balance>self.product_price:
            output='Here is your ' +self.product+' and $' +str(self.balance-self.product_price)+' change.'
            self.balance=0
            self.num_of_product-=1
            return output
        else:
            self.balance=0
            self.num_of_product-=1
            return 'Here is your candy.'
    def restock(self, number):
        self.num_of_product=number
        return 'Current ' + self.product+ ' stock: '+str(self.num_of_product)
    def deposit(self, money):
        self.balance+=money
        if self.num_of_product<1:
            return 'Machine is out of stock. Here is your $'+str(self.balance)+'.'
        else:
            return 'Current balance: $'+str(self.balance)



class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    >>> fussy_three = MissManners(3)
    >>> fussy_three.ask('add', 4)
    'You must learn to say please first.'
    >>> fussy_three.ask('please add', 4)
    'Thanks for asking, but I know not how to add'
    >>> fussy_three.ask('please __add__', 4)
    7
    """
    "*** YOUR CODE HERE ***"

    #the key is that the word after the please, put it after the MissManner arguments.
    #and then interate through the args tuple. 

    #what ask did is that to get the first argument of args and put the [7:] part as keyword to examine the corresponding function.
    # and the inputs are the remaining part in args. 



    def __init__(self, name):
        self.name=name

    def ask(self, *args):
        if args[0][0:6]!="please":
            return 'You must learn to say please first.'
        elif len(args[0][7:])>10:
            return 'Thanks for asking, but I know not how to '+args[0][7:]
        else:
            if args[0][7:]=="ask":
                return 'Current balance: $10'
            elif args[0][7:]=="add":
                return 'Thanks for asking, but I know not how to add'
            elif args[0][7:]=="__add__":
                return self.name.__add__(args[-1])
            elif args[0][7:]=="deposit":
                if self.name.__class__.__name__=='MissManners':
                    return 'Thanks for asking, but I know not how to '+args[0][7:]
                else:
                    return self.name.deposit(args[-1])
            elif args[0][7:]=="vend":
                return self.name.vend()
            
        









