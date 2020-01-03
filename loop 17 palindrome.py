#write a program to find a number is palindrome or not
n = int(input())
temp=n
reverse=0
while(n>0):
  dig = n % 10
  reverse = (reverse *10) + dig
  n=n//10
print(reverse)
if temp==reverse:
  print("palindrome")
else:
  print("not palindrome")

#codded by chithra
