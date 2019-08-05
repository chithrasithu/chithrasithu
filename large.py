nu1 = int(input(""))
nu2 = int(input(""))
nu3 = int(input(""))
 
if (nu1 > nu2) and (nu1 > nu3):
   largest = nu1
elif (nu2 > nu1) and (nu2 > nu3):
   largest = nu2
else:
   largest = nu3
 
print(largest)
