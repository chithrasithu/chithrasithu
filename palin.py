n=int(input(" "))
temp=n
rev1=0
while(n>0):
    dig=n%10
    rev1=rev1*10+dig
    n=n//10
if(temp==rev1):
    print("yes")
else:
    print("no")
