act = []
bet = []

# v5- Won 60% out of 5 games, brought in $1 total
# v5- Defeated v4 with a 70% win rate

def logic(money, points):
  bet.append(round(money * 0.01, 0))
  if points < 8 or points == 8:
    act.append("hit")
  elif points in [9, 10, 11, 12, 13, 14, 15, 16]:
    act.append("hit")
  elif points > 16:
    act.append("stand")
  return [act, bet]

def main(money, points):
  return logic(money, points)
