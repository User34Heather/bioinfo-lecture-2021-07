num = int(input("Which times table: "))
if 1 <= num <= 9:
    for i in range(1, 10):
        print(f"{num} * {i} = {num*i}")
else:
    print("What?")
