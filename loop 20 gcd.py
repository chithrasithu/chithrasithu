#write the code to gcd of a number
in1 = int(input())
in2 = int(input())
print("gcd of a number")
for i in range(1,in1+1):
  if in1 % i == 0 and in2 % i == 0:
    gcd=i
print(gcd)
