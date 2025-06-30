# ROCK ,PAPER,SCISSOR GAME
#RULES:
# 1.rock wins against scissors
# 2.scissor wins against paper
# 3.paper wins against rock

import random
print("!!!! WELCOME TO THE ROCK , PAPER , SCISSOR GAME !!!!")
rock=0
paper=1
scissor=2
user=int(input("Enter 0 for rock , 1 for paper , 2 for scissor:"))
print("user throw =",user)
computer=random.randint(0,2)
print("computer is =",computer)
if user == computer:
    print("game is tie")
elif user>computer:
    print("user wins the game!!")
elif user<computer:
    print("comp wins the game!!")
elif user==0 and computer==2:
    print("user wins the game!!")
elif user==2 and computer==0:
    print("computer wins the game!!")
