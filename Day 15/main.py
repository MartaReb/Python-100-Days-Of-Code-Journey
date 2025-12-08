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

money_in_machine = 0

def check_resources(choice):
    for item, amount in MENU[choice]["ingredients"].items():
        if resources[item] < amount:
            print(f"Sorry, not enough {item}.")
            return False
    return True

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money_in_machine}")

def calc_money(q, d, n, p):
    return q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01


while True:
    user_choose = input("What would you like? (espresso/latte/cappuccino) > ")

    if user_choose == "off":
        break
    elif user_choose == "report":
        print_report()
        continue
    elif user_choose in MENU:
        if not check_resources(user_choose):
            continue

        print("Please insert coins.")
        quarters = int(input("How many quarters? > "))
        dimes = int(input("How many dimes? > "))
        nickles = int(input("How many nickles? > "))
        pennies = int(input("How many pennies? > "))

        money = calc_money(quarters, dimes, nickles, pennies)
        cost = MENU[user_choose]["cost"]
        if money < cost:
            print("Sorry that's not enough money. Money refunded.")
            continue
        else:
            change = round(money - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            money_in_machine += cost

            # Subtracting components
            for item, amount in MENU[user_choose]["ingredients"].items():
                resources[item] -= amount

            print(f"Here is your {user_choose} ☕️. Enjoy!")

    else:
        print("Unknown command.")