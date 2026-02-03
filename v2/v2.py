# Won 20% out of 5 games
import random
def main(money, points):
	act = []
	bet = []
	# 5 is numbers 1 through 5, 9 is 6-10 along with royals
	nextcard = random.choice([5, 9])
	if money < 25:
		if points > 15:
			if nextcard == 5:
				act.append("hit")
			elif nextcard == 9:
				act.append("stand")
		elif points < 15:
			if nextcard == 9:
				act.append("hit")
			elif nextcard == 5:
				act.append("hit")
		elif action == hit:
			bet.append(0)
	elif money > 25:
		if points > 15:
			if nextcard == 5:
				act.append("hit")
			elif nextcard == 9:
				act.append("stand")
		elif points < 15:
			if nextcard == 9:
				act.append("hit")
			elif nextcard == 5:
				act.append("hit")
	action = act[0]
	if action == "hit":
		bet.append(round(money * 0.05, 0))
	elif action == "stand":
		bet.append(0)
	return [act[0], bet[0]]
