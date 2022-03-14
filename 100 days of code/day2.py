print("Welcome to the tip caculator!")
bill = float(input("What is the total bill?"))
tip = float(input("What percentage tip would you like to give?10,12 or 15?"))
num = float(input("How many people to split the bill?"))
res = (bill + tip*bill/100)/num
print(round(res,2))
