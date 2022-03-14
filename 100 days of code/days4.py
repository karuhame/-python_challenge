import random as r
""" #random exercise
#choose random head or tail
random_flip = r.randint(0,1)
if(random_flip==0): print("Tails")
else: print("Heads") 
"""
""" #Banker roulett
names = input().split(',')
ran = r.randint(0,len(names)-1)
print(ran)
print(names[ran])
 """
""" #Nested lists
sport= ["football", "volleyball", "basketball","tennis", "ping pong","kendo"]
solo_sport = ["tennis", "ping pong","kendo"]
team_sport = ["football", "volleyball", "basketball"]
sport = [solo_sport,team_sport]
print(sport) """
""" #Tresure Map
row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
map = [row1,row2, row3]
position = input("Where do you want to put the treasure?")
col = int(position[0])
row = int(position[1])
map[row-1][col-1] = "X"
print(*map,sep = "\n")
"""
""" #Rock, paper, scissors
player = int(input("What do you choose?Type 0 for Rock, 1 for Paper and 2 for Scissors"))
choice = ["rock","paper","scissors"]
computer = r.randint(0,2)
print("Player chose ",choice[player])
print("Computer chose", choice[computer])
if(player>=3 or player <0): print("You typed an invalid number you lose")
else:  
    if(computer==0 and player == 2): print("You lose!!!")
    elif(computer==2 and player == 0): print("You won!!!")
    elif(computer == player): print("Draw!!!")
    elif(computer > player): print("You lose")
    else: print("You won!!!")
"""