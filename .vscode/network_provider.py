#write a program that allows users to purchase data, purchase airtime, check data_balance, check airtime_balance
#set the airtime_balance to 1000(NGN), and data balance to 10(GB)
data_balance = 10.0 #GB
airtime_balance = 1000.0 #NGN
print("""
1) purchase data
2) purchase airtime
3) check data balance
4) check airtime balance
""")
selected_option = float(input("Select a number from 1 to 4: "))
if selected_option == 1:
    print("How much data do you want (GB)")
    data_amount = float(input("> "))
    print(f"Your data purchase of {data_amount}GB has been successful, This is your available balance {data_amount + data_balance} GB")
elif selected_option == 2:
    print("How much airtime do you want to buy: ")
    airtime_amount = float(input(">: "))
    print(f"Yello! your purchase of {airtime_amount}NGN has been completed. This is your available airtime balance {airtime_balance + airtime_amount}NGN")
elif selected_option == 3:
    print(f"Your data is remaining {data_balance} GB")
elif selected_option == 4:
    print(f"Total airtime balance is {airtime_balance} NGN")
else:
    print("enter a valid option: ")
