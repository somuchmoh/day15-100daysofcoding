from menu import MENU, resources
make_coffee = True
while make_coffee:
    # TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino): "
    order = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt
    if order == 'off':
        print("Coffee machine has been turned off 📴")

    # TODO 3: Print report
    if order == 'report':
        print(resources)

    # TODO 4: Check resources sufficient?
    if MENU[order]['ingredients']['coffee'] < resources['coffee'] and MENU[order]['ingredients']['water'] < resources['water'] and MENU[order]['ingredients']['milk'] < resources['milk']:

        # TODO 5: Process coins.
        money = 0
        amt_inserted = []
        print("Please insert coins")
        amt_inserted.append(int(input("How many quarters?: ")))
        amt_inserted.append(int(input("How many dimes?: ")))
        amt_inserted.append(int(input("How many nickels?: ")))
        amt_inserted.append(int(input("How many pennies?: ")))
        total_amount = amt_inserted[0] * 0.25 + amt_inserted[1] * 0.15 + amt_inserted[2] * 0.05 + amt_inserted[3] * 0.01
        print(f"Total amount inserted ${total_amount}")

        # TODO 6: Check transaction successful?
        if total_amount == MENU[order]['cost']:
            money += MENU[order]['cost']
        elif total_amount > MENU[order]['cost']:
            change = total_amount - MENU[order]['cost']
            print(f"Here is your change: ${change}")
            money += MENU[order]['cost']
        elif total_amount < MENU[order]['cost']:
            print("Sorry that's not enough money. Money refunded")

        # TODO 7: Make Coffee
        if order in MENU:
            resources['coffee'] = resources['coffee'] - (MENU[order]['ingredients']['coffee'])
            resources['water'] = resources['water'] - (MENU[order]['ingredients']['water'])
            resources['milk'] = resources['milk'] - (MENU[order]['ingredients']['milk'])
            print(f"Enjoy your {order}! ☕️")
            print(resources)
    else:
        make_coffee = False
        print("Not enough ingredients to make coffee")


