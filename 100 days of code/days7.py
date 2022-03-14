import random
#import word list
word_list = ["advark","baboon","camel"]
word = random.choice(word_list)
screen = ['_']*len(word)
lives = 6
print(word)

print(screen)
while(lives>0 and ('_'in screen)):
    guess = str(input().lower())
    if(guess not in word):
        print("You wrong~~~")
        lives-=1
        print(f"You have {lives} left")
    else:
        for i in range(len(word)):
            if(guess == word[i]):
                screen[i]= guess
    print(screen)

if(lives>0): print("You won!!!")
else: print("You lose")
