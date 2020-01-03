#write a program to print last and first dig of a number
n = int(input())
lis = []
print("dig count")
while(n>0):
  dig = n % 10
  lis.append(dig)
  n=n//10
print("last dig",lis[0])
print("first dig",lis[-1])
#codded by chithra
