string = input(" ")
count = 0
for a in string: 
    if (a.isspace()) == True: 
        count+=1
str = len(string)
char = str -count
print(char)
