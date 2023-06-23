commands = [
    "balance",
    "sale",
    "purchase",
    "account",
    "list",
    "warehouse",
    "review",
    "end",
]
balance = 0.0
amount = 0
warehouse = {}
operations = []
while True:
    print("- balance")
    print("- sale")
    print("- purchase")
    print("- account")
    print("- list")
    print("- warehouse")
    print("- review")
    print("- end")
    user_input = input("Enter one of the above options: ")
    user_input = user_input.strip()
    if user_input in commands:
        if user_input == commands[0]:
            while True:
                balance_choice = int(input("Please choose to Deposit(1), Withdraw(2), Print Balance(3) or End(4): "))
                if balance_choice == 1:
                    amount = float(input("Please enter the amount in '€': "))
                    balance += amount
                    operations.append(f"Added {amount}€ to balance, balance is {balance}")
                if balance_choice == 2:
                    amount = float(input("Please enter the amount in '€': "))
                    balance -= amount
                    operations.append(f"Withdrawn {amount}€ from balance, balance is {balance}")
                if balance_choice == 3:
                    print(f"Your balance is {balance} €: ")
                if balance_choice == 4:
                    break
                elif balance_choice < 1 or balance_choice >4:
                    print("Invalid input!")
                    print()

        if user_input == commands[1]:
            item_name = input("Please enter the item name: ")
            if item_name not in warehouse:
                print(f"{item_name} not present")
                continue
            item_amount = int(input("Please state the quantity: "))
            if warehouse[item_name]['quantity'] < item_amount:
                print("Insufficient quantity")
                continue
            item_price = float(input("Please state item price: "))
            warehouse[item_name]['quantity'] -= item_amount
            balance += item_price * item_amount
            operations.append(f"Sold {item_amount} of {item_name}, {item_price}€ each, Balance: {balance}")

        if user_input in commands:
            if user_input == commands[2]:
                item_name = input("Please enter the item name: ")
                item_amount = int(input("Please enter item quantity: "))
                item_price = float(input("Please enter item price: "))
                if item_name in warehouse:
                    if warehouse[item_name]['price'] == item_price:
                        warehouse[item_name]['quantity'] += item_amount
                if item_name not in warehouse:
                    warehouse[item_name] = {"price": item_price, "quantity": item_amount}
                    balance -= item_price * item_amount
                    if balance < item_price * item_amount:
                        balance += item_price * item_amount
                        print("Insufficient funds")
                        continue
                    operations.append(f"Bought {item_amount} of item: {item_name}, {item_price}€ each, Balance: {balance}")

        if user_input == commands[3]:
            print(f"Current balance is {balance}")
            operations.append(f"Checking balance, balance is {balance}€")

        if user_input == commands[4]:
            print("Total inventory in warehouse: ")
            for name, value in warehouse.items():
                print(f"{name} - {value}")
            operations.append("Checking inventory")

        if user_input == commands[5]:
            item_name = input("Enter item name to check status: ")
            if item_name in warehouse:
                for q,v in warehouse[item_name].items():
                    print(f"{q}: {v}")
                operations.append(f"Checking status of {item_name} in warehouse")
            else:
                print(f"{item_name} not present in warehouse")

        if user_input == commands[6]:
            from_index = int(input("Enter 'From' Index(press Enter to start from first operation): "))
            to_index = int(input("Enter 'To' index(press Enter to start from first operation)"))
            print()
            if from_index < 0 or to_index < 0 or from_index >= len(operations) or to_index >= len(operations):
                print("invalid range")
                continue
            if to_index <= from_index:
                print("To has to be bigger that from")
                continue
            for operation in operations[from_index:to_index]:
                print(operation)

        if user_input == commands[-1]:
            break

    else:
        print("Invalid input!")
        print()



