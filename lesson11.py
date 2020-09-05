def get_integer():
    return int(input("Give me a number: "))

def is_not_prime_number(user_input):
    for i in range(2,11):
        if num % i == 0:
            return True
    return False 
        
num = get_integer()
test = is_not_prime_number(num)
if test:
    print("Your number is not a prime number.")
else:
    print("Your number is a prime number!")


