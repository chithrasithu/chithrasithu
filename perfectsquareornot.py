import math
#for using square function
num1,num2=map(int,input().split())
number = num1 * num2
root = math.sqrt(number)
#for square root of a number
#checking perfect square or not
if int(root + 0.5) ** 2 == number:
	print("yes")
else:
	print("no")

