def deposit():
    print("welcome to deposit")
def withdraw():
    print("welcome to withdraw")
def check():
    print("welcome to check")
def sign_in(user_name,user_accountno):
    if uname.get(user_accountno) == user_name:
        print("sign_up successfully")
        print("choose your option")
        print("1.deposit")
        print("2.withdraw")
        print("3.check")
        choose=int(input())
        if choose == 1:
            deposit()
        elif choose == 2:
            withdraw()
        elif choose == 3:
            check()
        else:
            print("please enter your choice")
    else:
        print("please enter correct data")
        user_name=input("USER_NAME:  ")
        user_accountno=int(input("USER_ACCOUNTNO:  "))
        sign_up(user_name,user_accountno)
user_name=input("USER_NAME:  ")
user_accountno=int(input("USER_ACCOUNTNO:  "))
sign_in(user_name,user_accountno)
