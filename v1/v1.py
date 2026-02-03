"""
global act

v1 - 60% success rate

def logic(money, points):
  # Strategy: Careful, high roller
  act = []
  bet = []
  if money > 99:
    if points > 17:
      act.append("stand")
    elif points < 17:
      act.append("hit")
      bet.append(money * 0.25)
  elif money < 50:
    if points > 16:
      act.append("stand")
    else:
      act.append("hit")
      bet.append(money * 0.1)
  if len(bet) == 0:
    bet.append("no bet")
  if len(act) == 0:
    act.append("stand")
  print("Bot Move: ", act, "\nBot Bet:", bet)
"""
