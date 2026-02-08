# Simple Banking Application
balance = 0

def deposit(amount):
    global balance
    balance += amount
    
def withdraw(amount):
    global balance
    if (amount <= balance):
        balance -= amount

def check_balance():
    print(f" Current balance: {balance}")

while True:
    print("\n--- BANK MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            amt = int(input("Enter deposit amount: "))
            deposit(amt)

        case 2:
            amt = int(input("Enter withdraw amount: "))
            withdraw(amt)

        case 3:
            check_balance()

        case 4:
            print(" Thank you! Exiting...")
            break

        case _:
            print(" Invalid choice, try again")
