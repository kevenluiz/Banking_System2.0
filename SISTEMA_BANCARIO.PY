menu = """\033[1m\033[37mCHOOSE ONE OF THE OPTIONS BELOW:
\033[32m[ 1 ] DEPOSIT
\033[34m[ 2 ] WITHDRAW
\033[33m[ 3 ] STATEMENT
\033[31m[ 4 ] EXIT\033[0m
=> """

balance = 0
limit = 500
statement = []
num_withdrawals = 0
withdrawal_limit = 3

def deposit(amount):
    global balance
    balance += amount
    statement.append("\033[32mDeposit: $ {:.2f}\033[0m".format(amount))
    print("\033[32mYou made a deposit of $ {:.2f}\033[0m".format(amount))

def withdraw(amount):
    global balance, num_withdrawals
    balance -= amount
    statement.append("\033[34mWithdrawal: $ {:.2f}\033[0m".format(amount))
    num_withdrawals += 1

def show_statement():
    print("\033[33m°-°-" * 11)
    print("\033[33mSTATEMENT")
    if not statement:
        print("No transactions have been made.")
    else:
        for transaction in statement:
            print(transaction)
    print("\nBalance: $ {:.2f}".format(balance))
    print("\033[33m°-°-" * 11)

while True:
    option = input(menu)

    if option == "1":
        amount = float(input("\033[37mEnter the deposit amount: "))
        if amount > 0:
            deposit(amount)
        else:
            print("\033[31mInvalid operation. The amount entered is invalid.\033[0m")
    elif option == "2":
        amount = float(input("\033[37mEnter the withdrawal amount: "))
        if amount > 0:
            if amount > balance:
                print("\033[31mOperation failed! You do not have sufficient funds.\033[0m")
            elif amount > limit:
                print("\033[31mOperation failed! The withdrawal amount exceeds the limit.\033[0m")
            elif num_withdrawals >= withdrawal_limit:
                print("\033[31mOperation failed! Maximum number of withdrawals reached.\033[0m")
            else:
                withdraw(amount)
        else:
            print("\033[31mOperation failed! The amount is invalid.\033[0m")
    elif option == "3":
        show_statement()
    elif option == "4":
        print("\033[31mOPERATION TERMINATED! COME BACK SOON.\033[0m")
        break
    else:
        print("\033[31mINVALID INFORMATION. PLEASE TRY AGAIN.\033[0m")