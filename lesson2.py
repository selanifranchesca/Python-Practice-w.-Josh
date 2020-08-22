num = int(input("Give me a number: "))
if num % 2 == 0:
    print("The number is even")

elif num % 2 == 1:
        print("the number is odd")

if num % 4 == 0:
    print("the number is even and divisible by 4")

divisor = int(input("Give me a second number: "))
 
if num % divisor == 0:
    print("Divisor divides evenly into number.")

else:
    print("Divisor does not divide evenly into number.")