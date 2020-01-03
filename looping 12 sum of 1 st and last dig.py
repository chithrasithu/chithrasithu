#write a program to print sum of last and first dig of a number
n = int(input())
lis = []
print("dig count")
while(n>0):
  dig = n % 10
  lis.append(dig)
  n=n//10
  sumdig=lis[0]+lis[-1]
print(sumdig)
#codded by chithra
