# snake water and gun game
# snake, water gun  is a variation of the chindren game like rock paper and scissors.
# where players use hand gestures to represent a snake, water or gum. the gun beats the sanke, the waterbeats the gun and thesnake beats the water.
# write the python program to create s snake water gun game in python using if-else statement.
# do not create aby fancy GUI. use proper functiona to check for win.
    
import random

def check(comp, user):
    if comp == user:
        return 0
    
    if(comp ==0 and user ==1):
        return -1
    
    if(comp ==1 and user ==2):
        return -1
    if(comp ==2 and user ==0):
        return -1
    
    return 1
    
comp = random.randint(0,2)
user = int(input("0 for snake, 1 for water and 2 for gun : " ))
    
    
score = check(comp, user)
print("you: " ,user)
print("computer: ", comp)
if(score ==0):
    print("its a draw")
elif(score ==-1):
    print("you lose")
else:
    print("you won")
    