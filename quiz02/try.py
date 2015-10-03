n=15
coins=[1, 5, 10, 25]

def change(n, coins_avail, coins_so_far):
	if sum(coins_so_far)==n:
		yield coins_so_far
	elif sum(coins_so_far)>n:
		pass
	elif coins_avail==[]:
		pass
	else:
		for c in change(n, coins_avail[:], coins_so_far+[coins_avail[0]]):
			yield c
		for c in change(n, coins_avail[1:], coins_so_far):
			yield c

solution = [s for s in change(n, coins, [])]
print(max(solution, key= len))