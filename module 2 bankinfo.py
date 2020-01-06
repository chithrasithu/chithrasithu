def deposit():
    print("welcome to deposit")
def withdraw():
    print("welcome to withdraw")
def check():
    print("welcome to check")
def sign_up(user_name,user_accountno):
    if uname.get(user_accountno) == user_name:
        print("sign_up successfully")
        print("choose your option")
        print("1.deposit")
        print("2.withdraw")
        print("3.check")
        choose=input()
        if choose == "deposit":
            deposit()
        elif choose == "withdraw":
            withdraw()
        else:
            check()
    else:
        print("please enter correct data")
        user_name=input("USER_NAME:  ")
        user_accountno=int(input("USER_ACCOUNTNO:  "))
        sign_up(user_name,user_accountno)
user_name=input("USER_NAME:  ")
user_accountno=int(input("USER_ACCOUNTNO:  "))
sign_up(user_name,user_accountno)
