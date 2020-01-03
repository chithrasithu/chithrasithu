#write a program to swap 1st and last dig in the num
n = int(input())
lis = []
print("dig count")
while(n>0):
  dig = n % 10
  lis.append(dig)
  n=n//10
for i in lis:
  print(i,end="")
#codded by chithra
