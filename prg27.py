class Bank:
    def create(self):
        self.no = int(input("Enter account number: "))
        self.name = input("Enter account holder name: ")
        while True:
            self.fd = int(input("Enter FD amount: "))
            if self.fd < 500:
                print("Please deposit more than 500")
            else:
                print("Account created!")
                break

    def deposit(self):
        while True:
            namount = int(input("Enter amount to be deposited: "))
            if namount % 100 == 0:
                self.fd += namount
                print("Amount deposited!")
                break
            else:
                print("Enter multiples of 100!")

    def withdraw(self):
        while True:
            w_amount = int(input("Enter money to be withdrawn: "))
            if w_amount > self.fd:
                print("Entered amount exceeds balance")
            elif w_amount % 100 != 0:
                print("Can only withdraw amounts that are multiples of 100!")
            elif self.fd - w_amount < 500:
                print("Cannot withdraw money as it will leave balance below 500")
            else:
                self.fd -= w_amount
                print("Amount withdrawn!")
                break


bank = []

while True:
    print("\n1. A/C creation\n2. Money deposit\n3. Withdraw money\n4. Check balance\n5. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        account = Bank()
        account.create()
        bank.append(account)

    elif choice == 2:
        sacno = int(input("Enter account number to search: "))
        for account in bank:
            if account.no == sacno:
                print("Welcome", account.name)
                account.deposit()
                break
        else:
            print("No such account!")

    elif choice == 3:
        sacno = int(input("Enter account number to search: "))
        for account in bank:
            if account.no == sacno:
                print("Welcome", account.name)
                account.withdraw()
                break
        else:
            print("No such account!")

    elif choice == 4:
        sacno = int(input("Enter account number to search: "))
        for account in bank:
            if account.no == sacno:
                print("Welcome", account.name)
                print("Balance:", account.fd)
                break
        else:
            print("No such account!")

    elif choice == 5:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice! Please try again.")
