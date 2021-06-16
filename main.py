import random 

def play():
  user = input("WHATS YOUR CHOICE???'r' for rock, 'p' for paper, 's' for scissors...\n")

  computer = random.choice(['r', 'p', 's'])

  if user == computer :
    return 'IT IS A TIE'
#r>s, s>p, p>r
  if is_win(user, computer):
    return 'YOU WIN'
  return 'YOU LOST!!!!!'  
def is_win(player, opponent):
  if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
    return True

print(play())

