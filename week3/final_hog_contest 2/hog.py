"""This is a minimal contest submission file. You may also submit the full
hog.py from Project 1 as your contest entry."""

"""from functools import lru_cache
memoize=lru_cache(None)
"""

def memoize(f):
	data={}
	def lookup(*args):
		key=(f,args)
		if not key in data:
			data[key]=f(*args)
		return data[key]
	return lookup

GOAL_SCORE = 100

@memoize
def final_strategy(score, opponent_score):
    return best_num_to_roll(score,opponent_score)

final_bid = 7


def hog_wild(score, opponent_score):
	if (score+opponent_score)%7==0:
		return True
	else: 
		return False


def free_bacon_score(opponent_score):
	if opponent_score<10:
		return opponent_score+1
	else:
		singledigit=opponent_score%10
		tendigit=int(opponent_score/10)
		if singledigit>tendigit:
			return singledigit+1
		else: return tendigit+1


def is_prime_pro(score,opponent_score):
	n=score+opponent_score
	if n==0 or n==1:
		return False
	else:
		k=2
		while k<n:
			if n%k==0:
				return False
			k+=1
		return True

@memoize
def at_least(k,n,base): #base can only be 4 or 6
# n is the number of dice
	if k>0 and n==0:
		return 0
	elif k<=0 and n==0:
		return 1
	else:
		chance , outcome=0,2
		while outcome<=base:
			chance=chance+1/base*at_least(k-outcome,n-1,base)
			outcome+=1
		return chance


@memoize
def best_num_to_roll(score,opponent_score):
	sum_of_score=score+opponent_score
	if sum_of_score%7==6:
		if GOAL_SCORE- score>60:
			return 10
		else:
			return dice_should_roll(GOAL_SCORE- score,6)
	else:
		best_prob=0
		best_n=1
		for n in range(0, 11):
			prob=prob_of_winning_by_n(score,opponent_score,n)
			if prob>best_prob:
				best_prob=prob
				best_n=n
		return best_n

@memoize
def dice_should_roll(dream_score,base):
	return max(range(10), key=lambda n: at_least(dream_score,n,base))


def prob_to_pig_out(n,base):
	return 1-((base-1)/base)**n

@memoize
def prob_of_winning_by_n(score, opponent_score,n):
	base=6;
	if hog_wild(score,opponent_score):
		base=4
	prob_winning=0
	if n==0:
		turn_score=free_bacon_score(opponent_score)
		if is_prime_pro(score+turn_score,opponent_score):
			if score+turn_score>opponent_score:
				prob_winning=prob_winning_with_turn_end(score+2*turn_score,opponent_score)
			else:
				prob_winning=prob_winning_with_turn_end(score+turn_score,opponent_score+turn_score)
		else:
			prob_winning=prob_winning_with_turn_end(score+turn_score,opponent_score)
	else:
		for possible_score in range(1, (base*n)+1):
			prob_winning+=possible_scoring(possible_score,n,base)* prob_winning_with_turn_end(score+possible_score,opponent_score)
	return prob_winning

@memoize
def prob_winning_with_turn_end(score, opponent_score):
	if score>=GOAL_SCORE:
		return 1
	elif opponent_score>=GOAL_SCORE:
		return 0
	opponent_n_rolls=best_num_to_roll(opponent_score,score)
	prob_oppo_winning=prob_of_winning_by_n(opponent_score,score,opponent_n_rolls)
	return 1- prob_oppo_winning

@memoize
def number_to_score(k,n,s):
	if k<0:
		return 0
	if k==0 and n==0:
		return 1
	if n==0:
		return 0
	total=0
	for i in range(2,s+1):
		total+=number_to_score(k-i,n-1,s)
	return total

@memoize
def possible_scoring(k,n,s):
	if k==1:
		return 1-(pow(s-1,n)/pow(s,n))
	return number_to_score(k,n,s)/pow(s,n)















