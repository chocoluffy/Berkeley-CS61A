"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Roll DICE for NUM_ROLLS times. Return either the sum of the outcomes,
        or 1 if a 1 is rolled (Pig out). This calls DICE exactly NUM_ROLLS times.
        
        num_rolls:  The number of dice rolls that will be made; at least 1.
        dice:       A zero-argument function that returns an integer outcome.
        """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    "*** YOUR CODE HERE ***"
    i=1
    sum=0
    count=False
    while i<(num_rolls+1):
        m=dice()
        if m==1:
            count=True
        else: sum+=m
        i+=1
    if count:
        return 1
    else:
        return sum


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).
        
        num_rolls:       The number of dice rolls that will be made.
        opponent_score:  The total score of the opponent.
        dice:            A function of no args that returns an integer outcome.
        """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    "*** YOUR CODE HERE ***"
    if num_rolls==0:
        if opponent_score<10:
            return opponent_score+1
        else :
            tendigit=int(opponent_score/10)
            singledigit=opponent_score%10
            if tendigit>singledigit:
                return tendigit+1
            else: return singledigit+1
    else:
        return roll_dice(num_rolls, dice)



def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
        multiple of 7, in which case select four-sided dice (Hog wild).
        """
    "*** YOUR CODE HERE ***"
    sumofscore=score+opponent_score
    if sumofscore%7==0:
        return four_sided
    else: return six_sided

def is_prime(n):
    """Return True if a non-negative number N is prime, otherwise return
        False. 1 is not a prime number!
        """
    assert type(n) == int, 'n must be an integer.'
    assert n >= 0, 'n must be non-negative.'
    if n==0 or n==1:
        return False
    else:
        k = 2
        while k < n:
            if n % k == 0:
                return False
                k=k+1
            else: k=k+1
        return True


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.
        
        >>> other(0)
        1
        >>> other(1)
        0
        """
    return 1 - who

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
        Player 0's score first, and Player 1's score second.
        
        A strategy is a function that takes two total scores as arguments
        (the current player's score, and the opponent's score), and returns a
        number of dice that the current player will roll this turn.
        
        strategy0:  The strategy function for Player 0, who plays first
        strategy1:  The strategy function for Player 1, who plays second
        score0   :  The starting score for Player 0
        score1   :  The starting score for Player 1
        """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    "*** YOUR CODE HERE ***"
    while score0<goal and score1<goal:
        if who==0:
            this_round_zero=take_turn(strategy0(score0,score1), score1, dice=select_dice(score0, score1))
            score0+=this_round_zero
            # if score0!=score1:
            #     if is_prime(score0+score1):
            #         if score0>score1:
            #             score0+=this_round_zero
            #         else: score1+=this_round_zero
        else:
            this_round_one=take_turn(strategy1(score1,score0), score0, dice=select_dice(score1, score0))
            score1+=this_round_one

        if score0!=score1:
            if is_prime(score0+score1):
                if score0>score1:
                    score0+=this_round_one
                else: score1+=this_round_one
        who=other(who)
    return score0, score1  # You may want to change this line.

#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.
        
        A strategy is a function that takes two total scores as arguments
        (the current player's score, and the opponent's score), and returns a
        number of dice that the current player will roll this turn.
        
        >>> strategy = always_roll(5)
        >>> strategy(0, 0)
        5
        >>> strategy(99, 99)
        5
        """
    def strategy(score, opponent_score):
        return n
    return strategy

# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.
        
        To implement this function, you will have to use *args syntax, a new Python
        feature introduced in this project.  See the project description.
        
        >>> dice = make_test_dice(3, 1, 5, 6)
        >>> averaged_dice = make_averaged(dice, 1000)
        >>> averaged_dice()
        3.75
        >>> make_averaged(roll_dice, 1000)(2, dice)
        6.0
        
        In this last example, two different turn scenarios are averaged.
        - In the first, the player rolls a 3 then a 1, receiving a score of 1.
        - In the other, the player rolls a 5 and 6, scoring 11.
        Thus, the average value is 6.0.
        """
    "*** YOUR CODE HERE ***"
    def g(*args):
        i=0
        sum=0
        while i< num_samples:
            sum+=fn(*args)
            i+=1
        return sum/num_samples
    return g


def max_scoring_num_rolls(dice=six_sided):
    """Return the number of dice (1 to 10) that gives the highest average turn
        score by calling roll_dice with the provided DICE.  Assume that dice always
        return positive outcomes.
        
        >>> dice = make_test_dice(3)
        >>> max_scoring_num_rolls(dice)
        10
        """
    "*** YOUR CODE HERE ***"
    i=1
    max=1
    max_average=make_averaged(roll_dice,100)(1,dice)
    while i<11:
        temporary=make_averaged(roll_dice,100)(i,dice)
        if temporary>max_average:
            max_average=temporary
            max=i
        i+=1
    return max

def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1

def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate (0 to 1) of STRATEGY against BASELINE."""
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)
    return (win_rate_as_player_0 + win_rate_as_player_1) / 2 # Average results

def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False: # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)
    
   
    if False: # Change to True to test always_roll(4)
        print('always_roll(4) win rate:', average_win_rate(always_roll(4)))
    if True: # Change to True to test always_roll(5)
        print('always_roll(5) win rate:', average_win_rate(always_roll(5)))
    if False: # Change to True to test always_roll(6)
        print('always_roll(6) win rate:', average_win_rate(always_roll(6)))
    if False: # Change to True to test always_roll(7)
        print('always_roll(7) win rate:', average_win_rate(always_roll(7)))
    if False: # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))
   
    if False: # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))
    
    if True: # Change to True to test prime_strategy
        print('prime_strategy win rate:', average_win_rate(prime_strategy))
    if True: # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))
#   if True: # Change to True to test final_strategy
#        print('final_strategy_pro win rate:', average_win_rate(final_strategy_pro))
    
    "*** You may add additional experiments as you wish ***"

# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
        and rolls NUM_ROLLS otherwise.
        """
    "*** YOUR CODE HERE ***"
    if opponent_score<10:
        bacon_score=opponent_score+1
    else :
        tendigit=int(opponent_score/10)
        singledigit=opponent_score%10
        if tendigit>singledigit:
            bacon_score=tendigit+1
        else: bacon_score=singledigit+1
    if bacon_score<margin:
        return num_rolls
    else: return 0


def prime_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial boost and
        rolls NUM_ROLLS if rolling 0 dice gives the opponent a boost. It also
        rolls 0 dice if that gives at least MARGIN points and rolls NUM_ROLLS
        otherwise.
        """
    "*** YOUR CODE HERE ***"
    if opponent_score<10:
        bacon_score=opponent_score+1
    else :
        tendigit=int(opponent_score/10)
        singledigit=opponent_score%10
        if tendigit>singledigit:
            bacon_score=tendigit+1
        else: bacon_score=singledigit+1
    score+=bacon_score
    if is_prime(score+opponent_score):
        if score>opponent_score:
            return 0
        else:
            return num_rolls
    else:
        if bacon_score<margin:
            return num_rolls
        else:
            return 0

            

# def final_strategy(score, opponent_score, margin=9, num_rolls=5):
#        "*** YOUR CODE HERE ***"
#     if opponent_score<10:
#         bacon_score=opponent_score+1
#     else:
#         tendigit=int(opponent_score/10)
#         singledigit=opponent_score%10
#         if tendigit>singledigit:
#             bacon_score=tendigit+1
#         else: bacon_score=singledigit+1
#     score+=bacon_score
#     if is_prime(score+opponent_score):
#         if score>opponent_score+8:
#             return 0
#         elif score<opponent_score-20:
#             return 6
#         else:
#             if score>88 and score<95:
#                 return 4
#             elif score>94:
#                 return 3
#             elif score<30:
#                 return 6
#             else: return num_rolls
#     else:
#         if bacon_score<margin:
#             if score>88 and score<95:
#                 return 4
#             elif score>94:
#                 return 3
#             elif score<opponent_score-30:
#                 return 7
#             elif score<opponent_score-20:
#                 return 6
#             else: return num_rolls
#         else:
#             return 0



def final_strategy(score, opponent_score, margin=9, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial boost and
        rolls NUM_ROLLS if rolling 0 dice gives the opponent a boost. It also
        rolls 0 dice if that gives at least MARGIN points and rolls NUM_ROLLS
        otherwise.
        """
    "*** YOUR CODE HERE ***"
    if score<50 and (score+opponent_score)%7==6:
        return 7
    else:

        if opponent_score<10:
            bacon_score=opponent_score+1
        else :
            tendigit=int(opponent_score/10)
            singledigit=opponent_score%10
            if tendigit>singledigit:
                bacon_score=tendigit+1
            else: bacon_score=singledigit+1
        if (score+bacon_score)>100:
            return 0
        elif (score+bacon_score+opponent_score)%7==0:
            return 0
        else:
            if is_prime(score+opponent_score+bacon_score):
                if score>opponent_score+8: # since the
                    return 0
                elif score>opponent_score and (score+opponent_score+2*bacon_score)%7==0 :#if you lead and you can make your opponent worse, you make it
                    return 0
                elif score<opponent_score-40:
                    return 7
                elif score>opponent_score-40 and score<opponent_score-25:
                    return 6
                else:
                    if score>88 and score<95:
                        return 4
                    elif score>94:
                        return 3
                    else: return num_rolls
            else:
                if bacon_score<margin:
                    if score>88 and score<95:
                        return 4
                    elif score>94:
                        return 3
                    elif score<opponent_score-30:
                        return 7
                    elif score<opponent_score-20:
                        return 6
                    else: return num_rolls
                else:
                    return 0



# ######

# def memoize(f):
#     data={}
#     def lookup(*args):
#         key=(f,args)
#         if not key in data:
#             data[key]=f(*args)
#         return data[key]
#     return lookup

# GOAL_SCORE = 100

# @memoize
# def final_strategy(score, opponent_score):
#     return best_num_to_roll(score,opponent_score)

# final_bid = 7


# def hog_wild(score, opponent_score):
#     if (score+opponent_score)%7==0:
#         return True
#     else: 
#         return False


# def free_bacon_score(opponent_score):
#     if opponent_score<10:
#         return opponent_score+1
#     else:
#         singledigit=opponent_score%10
#         tendigit=int(opponent_score/10)
#         if singledigit>tendigit:
#             return singledigit+1
#         else: return tendigit+1


# def is_prime_pro(score,opponent_score):
#     n=score+opponent_score
#     if n==0 or n==1:
#         return False
#     else:
#         k=2
#         while k<n:
#             if n%k==0:
#                 return False
#             k+=1
#         return True

# @memoize
# def at_least(k,n,base): #base can only be 4 or 6
# # n is the number of dice
#     if k>0 and n==0:
#         return 0
#     elif k<=0 and n==0:
#         return 1
#     else:
#         chance , outcome=0,2
#         while outcome<=base:
#             chance=chance+1/base*at_least(k-outcome,n-1,base)
#             outcome+=1
#         return chance


# @memoize
# def best_num_to_roll(score,opponent_score):
#     sum_of_score=score+opponent_score
#     if sum_of_score%7==6:
#         if GOAL_SCORE- score>60:
#             return 10
#         else:
#             return dice_should_roll(GOAL_SCORE- score,6)
#     else:
#         best_prob=0
#         best_n=1
#         for n in range(0, 11):
#             prob=prob_of_winning_by_n(score,opponent_score,n)
#             if prob>best_prob:
#                 best_prob=prob
#                 best_n=n
#         return best_n

# @memoize
# def dice_should_roll(dream_score,base):
#     return max(range(10), key=lambda n: at_least(dream_score,n,base))


# def prob_to_pig_out(n,base):
#     return 1-((base-1)/base)**n

# @memoize
# def prob_of_winning_by_n(score, opponent_score,n):
#     base=6;
#     if hog_wild(score,opponent_score):
#         base=4
#     prob_winning=0
#     if n==0:
#         turn_score=free_bacon_score(opponent_score)
#         if is_prime_pro(score+turn_score,opponent_score):
#             if score+turn_score>opponent_score:
#                 prob_winning=prob_winning_with_turn_end(score+2*turn_score,opponent_score)
#             else:
#                 prob_winning=prob_winning_with_turn_end(score+turn_score,opponent_score+turn_score)
#         else:
#             prob_winning=prob_winning_with_turn_end(score+turn_score,opponent_score)
#     else:
#         for possible_score in range(1, (base*n)+1):
#             prob_winning+=possible_scoring(possible_score,n,base)* prob_winning_with_turn_end(score+possible_score,opponent_score)
#     return prob_winning

# @memoize
# def prob_winning_with_turn_end(score, opponent_score):
#     if score>=GOAL_SCORE:
#         return 1
#     elif opponent_score>=GOAL_SCORE:
#         return 0
#     opponent_n_rolls=best_num_to_roll(opponent_score,score)
#     prob_oppo_winning=prob_of_winning_by_n(opponent_score,score,opponent_n_rolls)
#     return 1- prob_oppo_winning

# @memoize
# def number_to_score(k,n,s):
#     if k<0:
#         return 0
#     if k==0 and n==0:
#         return 1
#     if n==0:
#         return 0
#     total=0
#     for i in range(2,s+1):
#         total+=number_to_score(k-i,n-1,s)
#     return total

# @memoize
# def possible_scoring(k,n,s):
#     if k==1:
#         return 1-(pow(s-1,n)/pow(s,n))
#     return number_to_score(k,n,s)/pow(s,n)





























##########################
# Command Line Interface #
##########################

# Note: Functions in this section do not need to be changed.  They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.
        
        This function uses Python syntax/techniques not yet covered in this course.
        """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')
    args = parser.parse_args()
                        
    if args.run_experiments:
                            run_experiments()

