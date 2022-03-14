import random as r
""" #average height
from string import hexdigits


list_heights=  list(map(float, input().split()))
sum = 0
for i in range(len(list_heights)):
    sum += list_heights[i]
sum/=len(list_heights)
print(round(sum,None)) """
""" #High score
students_score= list(map(int, input().split()))
mx = 0;
for i in students_score:
    if(i>mx):
        mx = i
print(f"The highest score in the class is: {mx}") """
""" #Sum of even
total = 0
for i in range(0,101,2):
    total += i
print(total) """
""" #FizzBuzz
for i in range(1,101):
    if(i%3==0 and i%5==0): print("FizzBuzz")
    elif(i%3 == 0): print("Fizz")
    elif(i%5 == 0): print("Buzz")
    else: print(i) """

""" #Password generator 
numbers = [str(x) for x in range(10)]
letter = 'qwertyuiopasdfghjklzcxvbnm'
letters = [str(x) for x in letter]
symbol = '!@#$%^&*()+'
symbols = [str(x) for x in symbol]
num_numbers = int(input("Number of number: "))
num_letters = int(input("Number of letters: "))
num_symbols = int(input("Number of symbols: "))
password = []
for i in range(num_numbers):
    password+= r.choice(numbers)
for i in range(num_letters):
    password+= r.choice(letters)
for i in range(num_symbols):
    password+= r.choice(symbols)
print(*password)
"""