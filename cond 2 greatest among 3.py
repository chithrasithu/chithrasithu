#write the code to print the gretest number between the 3 numbers
print("enter the numbers6")
num1,num2,num3 = map(int,input().split())
if num1 > num2 and num1 > num3:
  print(num1," is greater")
elif(num2 > num3):
  print(num2," is grater")
else:
  print(num3," is greater")


# codded by chithra
