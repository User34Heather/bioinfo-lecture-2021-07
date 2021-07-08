str1 = input("Enter s1: ")
str2 = input("Enter s2: ")

if len(str1) % 2 == 1 and len(str1) < len(str2):
    print(str1 + str2)
else:
    print(str2 + str1)
