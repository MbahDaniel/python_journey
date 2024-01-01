#store customers account
account = {
    "Daniel":{
        "account_number":123456789, 
        "pin": 2345,
        "balance":5000
        },
    "Chidi":{
        "account_number":345677893,
        "pin":4536,
        "balance":6780
        }
}

#Function to check pin
def checkpin(name,pin):
    if name in account:
        if account[name]["pin"]==pin:
            return True
    return False

#Function to check account balance
def checkbalance(name):
    if name in  account:
        return account[name]["balance"]
     

#Function to Withdraw money
def withdraw(name,amount):
    if name in account:
        if account[name]["balance"]>=amount:
            account[name]["balance"]-= amount
            return True
        return False
#  
def deposit(name,amount):
    if name in account:
        account[name]["balance"]+= amount
        return True
    return False


def main():
 while True:
    name =  input("Enter your name: ")
    pin = int(input("Enter your pin:  "))
    while True:
        if checkpin(name,pin):
            print("correct pin")
    
            print("""
                            1) Check Balance
                            2) Withdraw Money
                            3) Deposit Money
                            4) Exit
                        """)
        name =  input("Enter your name: : ")        
        Select  = int(input("Select a number: "))
        if Select == 1:
            balance = checkbalance(name)
            print(f"This is your current balance {balance}")

        elif Select ==2:
            amount = float(input("How much do you want to withdraw?"))
            if withdraw(name,amount):
                print("Withdraw successful!:")
            else:
                print("insufficient funds: ")
        elif Select == 3:
            amount = float(input("Enter the amount you want to deposit"))
            if deposit(name,amount):
                print("Deposit successful!")
            else:
                print("invalid account number: ")
        elif Select == 4:
            print("Thank you for using our ATM!")
        break
        #This will exit the loop and end the program
    

main()
