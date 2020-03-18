import random
import sys
from typing import List


def game(s):
    """
        :type s: str
    """
    l: List[str] = ["rock", "paper", "scissors"]
    a = random.choice(l)
    if s.lower() == a:
        print("It's a Draw")
        return 3
    else:
        if s.lower() == "rock":
            if a == "scissors":
                return 1
            else:
                return 2
        if s.lower() == "scissors":
            if a == "paper":
                return 1
            else:
                return 2
        if s.lower() == "paper":
            if a == "rock":
                return 1
            else:
                return 2


print("Welcome to the game of Rock Paper Scissors")
s_c = 0
s_u = 0
s = " "
while s.lower() != "exit":
    print("""Your Choices are:-
    Rock
    Paper
    Scissors
    Exit """)
    s = input("Enter your Choice:-- ")
    p1 = game(s)
    if p1 == 2:
        print("You lose😢😢😢")
        s_c += 1
    if p1 == 1:
        print("You win😄😄😄")
        s_u += 1
    if p1 == 3:
        print("It's a draw😌😌😌")
    print("""Score is 
    Computer :- %d
        User :- %d
        
        
        """ % (s_c, s_u))
else:
    sys.exit("Ending the game... Thanks for playing")
