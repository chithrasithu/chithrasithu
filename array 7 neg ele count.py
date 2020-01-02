#write a program to count negative element in array
l=list(map(int,input().split()))
count=0
for i in l:
  if i < 0:
    count=count+1
    
print("neg ele count",count)

  
#codded by chithra
