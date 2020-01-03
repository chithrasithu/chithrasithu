#write a program to reverse the number
n = int(input())
lis = []
while(n>0):
  dig = n % 10
  lis.append(dig)
  n=n//10
for i in lis:
  print(i,end="")
#codded by chithra
