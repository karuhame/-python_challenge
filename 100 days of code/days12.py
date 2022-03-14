#Randome num
import random
answer = random.randint(1,100)
#choose difficult
print("Welcome to Number Guessing Game.")
print("I'm thinking of a number between 1 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard.")
if(choice == "easy"):
    cnt = 10
else: cnt = 5
print(f"You have {cnt} turns to guess.")
#guess a number

#Check
while(cnt >0):
    guess = int(input("Make a guess: "))
    if(guess < answer): 
        cnt-=1
        print(f"Too low.You have {cnt} turns left.")
    elif(guess>answer):
        cnt-=1
        print(f"Too high.You have {cnt} turns left.")
    else:
        
        break
if(cnt==0):
    print(f"The answer is {answer}.Loser!!!")
else:
    print(f"You win. The answer is {answer}. CONGRATULATIONS!!!")


#repeat until true or run out of turn