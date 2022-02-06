# Simple rock, paper, scissor game in python
# made my enal

import random

def play():
    user = input("What's your choice? rock (R), paper (P), scissor (S) : \n").lower()
    print("------------------")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "it's a tie!"
    
    if is_win(user, computer):
        return "you won!!"
        
    return "You lost!!"

def is_win(player, opponent):
    # R > S, S > P, P > R
    if (player == 'R' and opponent == 's') or (player == 'S' and opponent == 'P') or (player == 'p' and opponent == 'r'):
        return True

print(play())