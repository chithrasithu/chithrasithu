#write a program to product  of the dig in the number
n = int(input())
pro1=1
while(n>0):
  dig = n % 10
  pro1=dig*pro1
  n=n//10
print("dig product",pro1)
#codded by chithra
