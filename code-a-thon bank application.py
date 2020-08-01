class account:  #account is user defined class
    def __init__(self): # constructor # to carry the variable within the same class but another function we mandatorily used SELF in our all functions in the class
        self.balance=5000 #minimum balance initially  
        print("Your Current and Minimum Account Balance is 5000 Rs/-")


    def acholder(self): # acholder is user defined class
        self.name=input("Enter account holder name") #to enter the name of account holder
        self.acnumber=int(input("Enter account number")) # to enter account number of account holder
        self.typeofaccount=input("Enter type of account") # to enter accountn type of account holder


    def disacholder(self): # disacholder is user defined class
        print("Acount holder name=",self.name) #to print name of the acount holder
        print("Account number=",self.acnumber) #to print the account number
        print("Type of account=",self.typeofaccount) # to print the type of account
         

    def deposit(self): # deposit is user defined class
        amount=int(input("Enter the amount to be deposited"))
        self.balance=self.balance+amount #to add the deposit amount into old balance
        print("Acount holder name=",self.name)
        print("Account number=",self.acnumber)
        print("Type of account=",self.typeofaccount)
        print("Your deposit is successful and the balance in account is %f" %self.balance)


    def withdraw(self): # withdraw is user defined class
        amount=int(input("Enter amount to be withdraw"))
        if(self.balance > amount): #withdrawals amount should not be more than the balance amount
            self.balance=self.balance-amount
            print("Acount holder name=",self.name)
            print("Account number=",self.acnumber)
            print("Type of account=",self.typeofaccount)
            print("The withdraw is successful")
        else:
            print("Insufficient Balance")


    def changeownername(self):
        self.name=input("Enter old owner name") #enter old account holder name
        self.newownername=input("Enter new owner name") #enter new account holder name
        self.name=self.newownername
        print("Owner name is been successfully changed")
        

        


#main
print("        ********** Detroit United Bank welcomes you **********        ")
print("     *** Welcome to Perform transaction for an account option ***     ")
print("\n 1.Deposit money in your account \n 2.Withdraw money from your account \n 3.Change the owner name \n 4.Display the transactions and closing balance \n 5.Exit")
choice=int(input("Please select your banking choice"))
if(choice==1):
    acc=account()
    acc.acholder()
    acc.deposit()
elif(choice==2):
    acc=account()
    acc.acholder()
    acc.withdraw()
elif(choice==3):
    acc=account()
    acc.acholder()
    acc.changeownername()
    acc.disacholder()
    
    
