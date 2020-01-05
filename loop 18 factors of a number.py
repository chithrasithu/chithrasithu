in1 = int(input())
print("factors of a number")
for i in range(1,in1+1):
  if in1 % i == 0:
    print(i,end=" ")
