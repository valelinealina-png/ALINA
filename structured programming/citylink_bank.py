def check_eligibility(age, account_type):
    if account_type == "T" and age > 25:
        return False
    else:
        return True


name = input("enter customer name: ")
age = int(input("enter age: "))
account_type = input("enteraccount type (S/C/T): ")

print("name:", name)
print("age:", age)
print("acccount_type:", account_type)

eligible = check_eligibility(age, account_type)
print("eligible:", eligible) 

def get_minimum_deposit(account_type):
    if account_type == "S":
        return 50000
    elif account_type == "C":
        return 100000
    elif account_type == "T":
        return 20000
    else:
        return 0

account_type = input("enter account type(S/C/T): ")
minimum = get_minimum_deposit(account_type)
print("minimum deposit:", minimum)

deposit = float(input("enter initial deposit: "))
if deposit >=minimum:
    print("deposit accepted")
else:
    print("deposit is too low")


def open_account():
    name = input("enter customer name: ")
    age = int(input("enter age: "))
    account_type = input("enter account type (S/C/T):")

    eligible = check_eligibility(age, account_type)
    if eligible:
        minimum = get_minimum_deposit(account_type)
        deposit = float(input("enter initial deposit: "))
        if deposit >= minimum:
            print("account opened successfully!")
            return deposit
        else:
            print("deposit is too low.")
            return None
    else:
        print("customer is not eligible")
        return None

balance = open_account()

def deposit(balance):
    amount = float(input("enter deposit amount: "))
    if amount > 0:
       balance += amount
       print("deposit successful.")
    else:
        print("invalid deposit.")
    return balance
balance = 80000
balance = deposit(balance)
print("new balance:", balance)

def withdraw(balance):
    amount = float(input("enter withdraw amount: "))
    if amount > 0 and amount <= balance:
        balance -= amount
        print("withdrawal successful.")
    else:
        print("invalid withdrawal.")
    return balance

balance = 105000
balance = withdraw(balance)
print("new balance:", balance)

