#write a program to sum of the dig in the number
n = int(input())
sum1=0
while(n>0):
  dig = n % 10
  sum1=dig+sum1
  n=n//10
print("dig sum",sum1)
#codded by chithra
