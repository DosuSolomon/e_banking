from random import randint
class E_banking:
    
    account_number = randint(1000000000,9999999999)
    account_info = {}
    account_details = []
    account_balance = 0
    balance = ""

    def __init__(self):
        print("Welcome to Access bank e-banking")

    def registration(self):

        self.account_info[self.account_number] = account_name
        print("your account number is:", self.account_number)
        print("Your account balance is #",self.account_balance)
        print(self.account_info)
        # print("value:", self.account_balance)

        # self.account_balance[account_number] = account_name

    def account_detailed(self):
        print(" Your account details is")
        for account in self.account_details:
            print(account)
        pass

    def save(self):
        return self.balance + deposit
    print(save)
    def withdraw(self):
        pass
    def chack_balance(self):
        self.balance
        print(self.balance)


access = E_banking()

while True:
    print("""
                Enter 1. To open account
                Enter 2. To check account details
                Enter 3. To deposit
                Enter 4. To withdraw
                Enter 5. To check balance
                Enter 6. To exit""")

    choice = int(input("Enter a selection: "))

    if choice is 1:
        first_name = input("Enter your first name: ")
        access.account_details.append("first name: "+first_name)
        last_name = input("Enter your last name: ")
        access.account_details.append("lastname: "+last_name)
        account_name = input("Enter your account name: ")
        access.account_details.append("account name: "+account_name)
        access.account_details.append("account number: %s" %access.account_number)
        access.registration()
#
    elif choice is 2:
        access.account_detailed()
    elif choice is 3:
        # while True:
        account_number = input("Enter account number: ")
        access.account_details.append(account_number)
        if account_number in access.account_details:
            deposit = input("Enter amount to deposit: ")
        else:
            print("Enter valid account number")
            break
        access.save()

    elif choice is 3:
        while True:
            account_number = input("Enter account number: ")

    elif choice is 4:
        access.chack_balance()
        # while True:
        #     account_number = input("Enter account number: ")

    elif choice is 5:
        while True:
            account_number = input("Enter account number : ")



