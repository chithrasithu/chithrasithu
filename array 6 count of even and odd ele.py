#write a program to count total number of odd and even element in array
l=list(map(int,input().split()))
odd = 0
even = 0
for i in l:
  if i % 2 != 0:
    odd=odd+1
  else:
    even=even+1
print("oddcount",odd)
print("evencount",even)
  
#codded by chithra
