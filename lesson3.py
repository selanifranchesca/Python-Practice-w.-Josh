a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
numbers = []
for number in a:
    if number < 5:
        numbers.append(number)
print(numbers)

maximum = int(input("Give me a number: "))
print("Your number is " + str(maximum))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
numbers = []
for number in a:
    if number < maximum:
        numbers.append(number)
print(numbers)