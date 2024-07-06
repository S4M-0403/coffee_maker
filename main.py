MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 25,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 35,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 50,
    }
}#dictionary that contains details of the drinks

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}#resources that are stored in the machine in the begin

profit = 0 #initial profit
should_continue = True

#function to check the resources available to make the drink
def check_resources(user_input):
    for item in user_input:
        if user_input[item] > resources[item]:
            print(f"Insufficient {item}.")
            return False
    return True

#function to calculate the sum of coins inputted by the user
def coins_process():
    print("Enter the coins: ")
    total = int(input("Enter the number of ₹1 coins: ")) *1
    total += int(input("Enter the number of ₹2 coins: ")) *2
    total += int(input("Enter the number of ₹5 coins: ")) *5
    total += int(input("Enter the numner of ₹10 coins: ")) *10
    return total

#function to return change as well as check if the transaction is complete or not
def transaction(payment, cost):
    if payment >= cost:
        change = payment - cost
        print(f"Your change is: ₹{change}")
        global profit 
        profit += cost
        return True
    else:
        print("Insufficient funds.")
        return False
                
#function which reduces the value of ingredients from the resources
def make_coffee(drink, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your ☕ {drink}. Enjoy!")    
    

while should_continue:
    user_input = input("​What would you like? (espresso/latte/cappuccino:)​ ").lower()
    if user_input == "off":
        should_continue = False
    if user_input == "report":
        print(f'Water : {resources["water"]}ml')
        print(f'Milk : {resources["milk"]}ml')
        print(f'Coffee : {resources["coffee"]}g')
        print(f'Cash : ₹{profit}')
    else:
        drink = MENU[user_input]
        if check_resources(drink["ingredients"]):
            payment = coins_process()
            if transaction(payment, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])