# A "simple" adventure game.

name = 'Player 1' # Can replace this with your name. :)
me = None # Will be initalized to Person(name) after Person class is defined

def adventure():
    while True:
        try: # In case of errors... catch them!
            check_win_conditions(me, Place)
            Place.current.describe()
            line = input('adventure> ')
            exp = adv_parse(line)
            output = adv_eval(exp)
            print(output)
            print('\n') # New line for neatness
        except (KeyboardInterrupt, EOFError, SystemExit): # If you ctrl-c or ctrl-d
            print('Bye!')
            return
        # If the player input was badly formed or if something doesn't exist
        except (SyntaxError, NameError, KeyError, TypeError, IndexError) as e:
            print('ERROR:', e)


def adv_parse(line):
    """ Parses adventure.py commands

    Handles things differently when
    the first part of the string is 'give'
    or 'ask'

    >>> adv_parse('look')
    ('look', '')
    >>> adv_parse('take rubber ducky')
    ('take', 'rubber ducky')
    >>> adv_parse('give rubber ducky to Andrew')
    ('give', 'rubber ducky', 'Andrew')
    >>> adv_parse('ask Andrew for advice about the midterm')
    ('ask', 'Andrew', 'advice about the midterm')
    """
    tokens = line.split()
    if not tokens: # empty list
        raise SyntaxError('No command given')
    token = tokens.pop(0) # https://docs.python.org/3/tutorial/datastructures.html

    if token == 'give':
        "*** YOUR CODE HERE ***"
        index_to= tokens.index('to')
        string= tokens[0]
        for i in range(1, index_to):
            string= string +' '+ tokens[i]
        string_left= tokens[index_to+1]
        for j in range(index_to+2, len(tokens)):
            string_left= string_left+ ' '+ tokens[j]

        return ('give', string, string_left)
    elif token == 'ask':
        "*** YOUR CODE HERE ***"
        index_for= tokens.index('for')
        string= tokens[0]
        for i in range(1, index_for):
            string= string +' '+ tokens[i]
        string_left= tokens[index_for+1]
        for j in range(index_for+2, len(tokens)):
            string_left= string_left+ ' '+ tokens[j]

        return ('ask', string, string_left)
    else: # Only split out the operator, the rest must be the operand
        "*** YOUR CODE HERE ***"
        return (token, line[(len(token)+1):])


def adv_eval(exp):
    """
    >>> from cs61a_world import *
    >>> Place.current = SodaHall
    >>> adv_eval(adv_parse('take rubber ducky'))
    'Player 1 takes the rubber ducky'
    >>> Place.current = WerdnasHouse
    >>> adv_eval(adv_parse('give rubber ducky to Werdna'))
    'Werdna takes the rubber ducky'
    """
    if is_operator(exp): # Use the underlying eval to grab the
        return eval(exp) # function that implements the action.
    if is_person(exp):
        return Person.people[exp]
    elif isinstance(exp, str): # If we're describing something,
        return exp             # just output it.
    elif exp[0] == 'stuff':
        print("You look through your stuff... you see")
        for item in me.inventory:
            return item.examine()
        

    elif exp[0] == 'give':
        "*** YOUR CODE HERE ***"
        first=Person(exp[2])
        Place.current.people.append(first)
        return give(first,exp[1])
    elif exp[0] == 'ask':
        "*** YOUR CODE HERE ***"
        second= Person(exp[1])
        Place.current.people.append(second)
        return ask(second,exp[2])
    else:
        "*** YOUR CODE HERE ***"
        return adv_apply(exp[0],exp[1])


def adv_apply(operator, operand):
    "*** YOUR CODE HERE ***"

    return eval(operator)(operand)

def is_person(exp):
    return exp in Person.people

def check_win_conditions():
    pass

# We shouldn't define the following functions in the global frame.  There are
# better ways of doing this (generic operator FTW), but for simplicity's sake,
# this is what I'm going with.

def is_operator(exp):
    return exp in ('look', 'go', 'take', 'give', 'ask',
                   'examine', 'help')

def look(_):
    return Place.current.look()

def go(direction):
    output = Place.current.exit_to(direction)
    return output

def take(thing):
    obj = Place.current.find(thing)
    if obj:
        return me.take(obj)
    return 'No such thing to take!'

def give(person, thing):
    if type(person) != Person:
        return "Who is {}?!".format(person)
    if person not in Place.current.people:
        return person.name + ' not here!'
    obj = None
    for i, e in enumerate(me.inventory):
        if thing in e.name:
            obj = me.inventory.pop(i)
    if obj:
        return person.take(obj)
    return "You don't have this in your possession!"

def ask(person, message):
    if type(person) != Person:
        return "Who is {}?!".format(person)
    if person not in Place.current.people:
        return person.name + ' not here!'
    return person.ask(message)

def examine(thing):
    for item in me.inventory:
        if thing in item.name:
            return item.examine()
    return "You don't have this in your possession!"

def help(_):
    return """There are 7 possible operators:
  * look
  * go [direction]
  * take [thing]
  * give [thing] to [person]
  * examine [thing in inventory]
  * ask [person] for [message]
  * help"""


# OOP representation of the game models:
class Person(object):
    people = {}
    def __init__(self, name, *things):
        self.name = name
        self.inventory = list(things)
        Person.people[name] = self

    def think(self, msg):
        return self.name + 'remains silent'

    def take(self, thing):
        self.inventory.append(thing)
        return self.name + ' takes the ' + thing.name

    def ask(self, msg):
        return self.think(self, msg)

    def go(self, direction):
        return

# Need to initalize after Person class exists
me = Person(name)


class Place(object):
    current = None
    def __init__(self, name, description, *people_and_things):
        self.name = name
        self.description = description
        self.people = []
        self.things = []
        self.exits = {}
        for obj in people_and_things:
            if type(obj) == Person:
                self.people.append(obj)
            elif type(obj) == Thing:
                self.things.append(obj)

    def describe(self):
        print(self.description)
        if self.exits:
            print('\nExits:')
            for k, v in self.exits.items():
                print('  ', k, '-', v[0].name)
        print()

    def look(self):
        result = 'You take a look around and see:\n'
        if not (self.people or self.things):
            result += 'Nothing!'
        result += '\n'.join([thing.name + ' - ' + thing.description for thing in self.things])
        result += '\n'.join([person.name for person in self.people])
        return result

    def exit_to(self, exit):
        if exit in self.exits:
            new_place, exit_msg = self.exits[exit]
            Place.current = new_place
            return exit_msg
        return "Where do you think you're going?!"

    def find(self, thing):
        for i, e in enumerate(self.things):
            if thing in e.name:
                return self.things.pop(i)


class Thing(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def examine(self):
        return self.description


# This is what @main does (sorta)
if __name__ == '__main__':
    try:
        # import readline # Why?

        from cs61a_world import *

        me = Person(name)
        print(motd)
        adventure()
    except ImportError as e:
        print("ERROR: Something terrible happened to " + world + ".py")
        print("\t Invalid or broken world.")
        print(e)
    except IndexError as e:
        print("ERROR: Could not load world. Did you forget to provide it?")
        print("\tExample: python3 adventure.py cs61as_world")
        print(e)

