sit = input("")
if sit == 'a' or sit == 'e' or sit == 'i' or sit == 'o' or sit == 'u':
	print("Vowel")
elif((sit>='a' and sit<= 'z') or (sit>='A' and sit<='Z')):
    print("Consonant")
else:
    print("invalid")
