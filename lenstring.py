char = int(input(""))
list1 = []
list2 = []
for i in range(0, char):
  instr = input(" ")
  list1.append(instr)
    
list2 = sorted(list1, key=len) 
print(list2[0])
