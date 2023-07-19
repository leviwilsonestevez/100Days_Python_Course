from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_machine_on = True

while is_machine_on:
    coffee_machine = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()
    choice = input(f"What would you like? ({menu.get_items()})")
    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink_item = menu.find_drink(choice)
        is_enough_resources = coffee_machine.is_resource_sufficient(drink_item)
        is_money_enough = money_machine.make_payment(drink_item.cost)
        if is_enough_resources and is_money_enough:
            coffee_machine.make_coffee(drink_item)
