MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def report(cur_resources):
    for i in cur_resources:
        print(f"{i} : {cur_resources[i]}")




def check_resources(client_order, cur_resources):
    for i in resources:
        x = MENU[client_order]["ingredients"][i]
        if(x >cur_resources[i]):
            print(f"Sorry. There is not enough{i}")
            return False
    return True

def process_coin(quarter,dimes,nickles, pennies, order,cur_resources):
    
    total = quarter*0.25+dimes*0.1+nickles*0.05+pennies*0.01
    if(total<MENU[order]["cost"]):
        print("Sorry, not enough. Money refunded.")
        return cur_resources, 0
    else:
        for i in resources:
            cur_resources[i] -= MENU[client_order]["ingredients"][i]
        cur_resources["money"] +=MENU[order]["cost"]
        change = total-MENU[order]["cost"]
        return cur_resources,change




    
should_continue = True
cur_resources = resources.copy()
cur_resources["money"] = 0
while should_continue:
    client_order = input("What would you like? (espresso/latte/cappuccino):").lower()
    if(client_order=="off"):
        print("You're welcome")
        break
    if(client_order=="report"):
        report(cur_resources)
    else:
        if(check_resources(client_order,cur_resources)):
            print("GIMME MONEY")
            quarter = int(input("how many quarter?"))
            dimes = int(input("how many dimes?"))
            nickles = int(input("how many nickles?"))
            pennies = int(input("how many pennies?"))
            cur_resources, change = process_coin(quarter,dimes,nickles, pennies, client_order,cur_resources)
            if(change != 0):
                print(f"Here is ${change} dollars in change")
            print(f"Here is your {client_order}. Enjoy!")
        
        else:
            print("Sorry.We run out of resources.")
            continue