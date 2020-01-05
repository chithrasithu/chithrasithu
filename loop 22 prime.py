#write the code to find wheather the number is prime or not
print("enter the number")
num1 = int(input())
def prime(x):
  div=x//2
  count=0
  for i in range(2,div):
    if x % i == 0:
      count=count+1
  if count==0:
    print("prime")
  else:
    print("not prime")

prime(num1)
  

# codded by chithra
