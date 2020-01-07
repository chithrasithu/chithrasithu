def login():
  print("login")
def sign_in():
  print("sign_in")
print("WELCOME TO CHITHRAMEERA BANK")
print("ENTER YOUR CHOICE")
print("1.LOGIN")
print("2.SIGN_IN")
user_need=int(input())
if user_need==1:
  login()
elif user_need==2:
  sign_in()
else:
  print("please choose the choice")

  
