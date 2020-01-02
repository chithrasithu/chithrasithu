#write a program to print 2 nd largest  element in array
l=list(map(int,input().split()))
len1 = 0
for i in l:
  len1=len1+1
for i in range(len1):
    for j in range(i + 1, len1):

        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]
print("second largest element")
print(l[len1-2]) 
#codded by chithra
