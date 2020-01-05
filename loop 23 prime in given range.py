#write the code to print the prime number in given range
print("enter the number")
num1 = int(input())
print("prime numbers")
def prime(x):
  for j in range(2,x+1):
    count=0
    for i in range(2,j):
      if j % i == 0:
        count=count+1
    if count==0:
      print(j)

prime(num1)
  

# codded by chithra
