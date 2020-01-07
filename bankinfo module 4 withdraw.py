balance={3456:67878,67689:567}
histry={7:8908}
def main_menu():
    print("main menu")

def withdraw(user_accountno):
    withdraw_amount=int(input("enter withdraw amount"))
    histry.update({user_accountno:withdraw_amount}) 
    if balance.get(user_accountno) >= withdraw_amount:
        total_balance=balance.get(user_accountno)-withdraw_amount
        balance[user_accountno] = total_balance
        print("current balance",balance.get(user_accountno))
    else:
        print("your balance insufficient")
    user_need=input("continue or exit")
    if user_need == 'continue':
       main_menu()
    else:
       print("thanks for using chittu atm")
    
	
withdraw(3456)
f = open("bankinfo.txt", "w")
f.write(str(balance))
f.write(str(histry))

