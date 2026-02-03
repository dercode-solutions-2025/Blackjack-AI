# Experimental hi-low reinforcement learning bot.
# Won 40% out of 5 games, lost $42
# v4- Lost to v5
act = []
bet = []
final = {
  "action": None,
  "bet": None
}

def reinforce(status):
  if status < 0:
    decision = "careful"
  elif status > 0 and status < 50 or status == 50:
    decision = "standard"
  elif status > 50:
    decision = "risky"
  return decision

def initialbet(money):
  status = reinforce(money)
  if status == "careful":
    bet.append(5)
  elif status == "standard":
    bet.append(money * 0.25)
  elif status == "risky":
    bet.append(money * 0.5)
  return bet

def careful(points):
  if points > 15:
    act.append("stand")
  elif points < 15:
    act.append("hit")
  return act

def standard(points):
  if points < 11:
    act.append("hit")
  elif points > 16:
    act.append("stand")
  else:
    act.append("hit")
  return act

def risky(points):
  if points < 17:
    act.append("hit")
  elif points > 17:
    act.append("stand")
  elif points == 17:
    act.append("stand")
  return act

def main(money, points):
  decision = reinforce(money)
  final["bet"] = initialbet(money)
  if decision == "careful":
    final["action"] = careful(points)
  elif decision == "standard":
    final["action"] = standard(points)
  elif decision == "risky":
    final["action"] = risky(points)
  return final
