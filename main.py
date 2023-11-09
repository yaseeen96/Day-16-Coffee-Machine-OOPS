from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_machine_off = False

# cappuccino = MenuItem("cappuccino", 400, 500, 400, 2.5)
# latte = MenuItem("latte", 200, 500, 400, 3.25)
# espresso = MenuItem("espresso", 200, 500, 400, 4.0)

print("Welcome to my coffee machine")
print("MENU")
items = menu.get_items().split("/")
for item in items:
    print(item)

while not is_machine_off:
    decision = input("What would you like to buy?: ")
    if decision == "cappuccino" or decision == "espresso" or decision == "latte":
        drink = menu.find_drink(decision)
        confirm_order = input(f"{drink.name} would cost you ${drink.cost}. Enter 'y' to purchase it. 'b' to go back: ")
        if confirm_order == "y":
            is_resource_sufficient = coffee_maker.is_resource_sufficient(drink)
            if is_resource_sufficient:
                is_money_received = money_machine.make_payment(drink.cost)
                if is_money_received:
                    coffee_maker.make_coffee(drink)
                    print("Thank you for using my coffee machine.")
                    continue
                else:
                    print("Please come back later. ")
                    break
        else:
            continue

    elif decision == "report":
        coffee_maker.report()

    elif decision == "off":
        print("Coffee machine turned off successfully.")
        is_machine_off = True
