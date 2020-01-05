#write the code to lcm of a number
print("enter the numbers")
num1 = int(input())
num2 = int(input())
def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
print("The L.C.M. is", compute_lcm(num1, num2))
  

# codded by chithra
