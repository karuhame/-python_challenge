print("""
Welcome to Treasure Island.
Your mission is to find the treasure.
""")
choice = input("Your are at a cross road. Where do you want to go? Left or right?").lower()
if(choice=="right"):
    choice = input("You've come to a lake. There is a island in the middle of the lake.Wait for the boat or swim across. Type wait or swim").lower()
    if(choice=="wait"):
        choice = input("You're at the island unharmed. There is a house with 3 doors. One red, one blue, one yellow. Which color do you choose?").lower()
        if (choice == "red"):
            print("You win!!!")
        else: print("Game over")
    else:
        print("Game over")
else:
    print("Game over")