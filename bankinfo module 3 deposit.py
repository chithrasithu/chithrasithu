balance={3456:67878,67689:567}
histry={7:8908}
def main_menu():
    print("main menu")

def deposit(user_accountno):
    deposit_amount=int(input("enter deposit amount"))
    histry.update({user_accountno:deposit_amount}) 
    total_balance=balance.get(user_accountno)+deposit_amount
    balance[user_accountno] = total_balance
    print(balance.get(user_accountno))
    print(histry)
    user_need=input("continue or exit")
    if user_need == 'continue':
       main_menu()
    else:
       print("thanks for using chittu atm")
    
	
deposit(3456)
f = open("bankinfo.txt", "w")
f.write(str(balance))
f.write(str(histry))

