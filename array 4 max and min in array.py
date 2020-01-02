#write a program to print maximum and minimum element in array
l=list(map(int,input().split()))
len1 = 0
for i in l:
  len1=len1+1
for i in range(len1):
    for j in range(i + 1, len1):

        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]


print("maximum")
print(l[len1-1]) 
print("minimum")
print(l[0])
#codded by chithra
