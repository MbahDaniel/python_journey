#Write a code on how an ATM machine works, with an avalaible balance of a balance of 1000.00 (NGN)


print("Welcome to Daniel bank: ")
print("""
1) Withdraw Money
2) Deposit Money
3) Transfer Money
4) Check balance 
5) Exit 
      """)
balance = 1000.00 #NGN
Select  = int(input("Select a number: "))
if Select == 1:#withdraw money
    amount = float(input(f"how much do you want to withdraw: "))
    if amount <= balance:
        print(f"Your withdrawal of {amount} (NGN) was successful")
    else:
        print("Insufficient balance: ")
elif Select == 2:#Deposit Money
    dep_amount = float(input("Enter the amount you want to deposit: "))
    balance += dep_amount
    print("deposit was successful: ")
elif Select == 3: #transfer money
 banks = {"daniel",}
 trans_amount= int(input("how much do you want to transfer"))
 if balance <= trans_amount:
     print(f"Your transfer of {trans_amount}(NGN) was sucessful! {balance-trans_amount} (NGN) is your available balance: ")
 else:
     print(f"Your transfer of {trans_amount} (NGN) was not successful!, This is your available balance {balance} (NGN)")
elif Select  == 4:#show available balance
    print(f"This is your avalable balance {balance} (NGN)")
elif Select == 5:#exit
    print("Thanks for using Daniel's ATM!")
else:#Selected an invalid number
    print("Invalid option. Please try again!")


