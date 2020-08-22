number = int(input("Give me a number: "))
numbers = range(0,100)
for a in numbers:
    if a % number == 0:
        print(a)
