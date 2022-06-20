import sys

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

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}

def prompt_user():
    answer = input("What would you like to drink? (espresso/latte/cappuccino)")
    if answer == "off":
        print("Machine is shutting down")
        sys.exit(0)
    elif answer == "report":
        report()
    else:
        for drink in MENU:
            if answer == drink:
                return answer            
        print("Invalid drink choice, please select from espresso/latte/cappuccino")
        prompt_user()

def report():
    for resource in resources:
        if resource in ["milk", "water"]:
            unit = "ml"
        elif resource in ["coffee"]:
            unit = "g"
        else:
            unit = " USD"
        print(f"{resource}: {resources[resource]}{unit}")
    prompt_user()

def check_sufficient(drink):
    for substance, value in MENU[drink]["ingredients"].items():        
        result = int(resources[substance]) - int(value)
        if result < 0:
            print(f"Insufficent {substance}")
            return False
        else:
            return True

def get_value_of_coins(number, type):
    value = number * coins[type]
    return value

def process_coins(drink):
    money = 0
    for coin in coins:
        number_of_coins = 0
        number_of_coins += int(input(f"Insert number of {coin}: "))
        money += get_value_of_coins(number_of_coins, coin)
    if money == MENU[drink]["cost"]:
        resources["money"] += money
        make_drink(drink)
    elif money > MENU[drink]["cost"]:
        change = money -  MENU[drink]["cost"]
        resources["money"] += MENU[drink]["cost"]
        print(f"Change returned: {round(change, 2)}")
        make_drink(drink)
    else:
        print(f"Insufficient coin value received, refunded")
        run()

def make_drink(drink):
    for substance, value in MENU[drink]["ingredients"].items():
        if not substance == "money":
            resources[substance] -= int(value)
    print(f"Here is your {drink}")

def run():
    drink = prompt_user()
    if not "money" in resources:
        resources["money"] = float(0)
    if check_sufficient(drink):
        process_coins(drink)
    # Call itself to start the process again with current resources
    run()

if __name__ == "__main__":
    run()