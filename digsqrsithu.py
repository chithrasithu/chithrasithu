num = int(input(""))
sum=0
while(num>0):
  dig=num%10
  sum=sum+dig**2
  num=num/10
sum = int(sum)
print(sum)
