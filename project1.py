# ROCK ,PAPER,SCISSOR GAME
#RULES:
# 1.rock wins against scissors
# 2.scissor wins against paper
# 3.paper wins against rock

import random
rock=0
paper=1
scissor=2
user=int(input("Enter 0 for rock , 1 for paper , 2 for scissor:"))
print("user is =",user)
comp=random.randint(0,2)
print("comp is =",comp)
if user == comp:
    print("game is tie")
elif user>comp:
    print("user win")
elif user<comp:
    print("comp")
elif user==0 and comp==2:
    print("user win")
elif user==2 and comp==0:
    print("comp win")