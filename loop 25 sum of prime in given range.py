#write the code to print sum of prime  numbers in given range
print("enter the number")
num1 = int(input())
print("sum of prime numbers")
def prime(x):
  sum1=0
  for j in range(2,x+1):
    count=0
    for i in range(2,j):
      if j % i == 0:
        count=count+1
    if count==0:
      sum1=sum1+j
  print(sum1)

prime(num1)


# codded by chithra
