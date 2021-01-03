num = int(input("Give me a number__:"))
def fib(num):
    first = 0
    second = 1

    if num == 0:
        return 0
        
    if num < 1: 
        return -1

    if num == 1:
        return first 

    if num == 2: 
        return second

    count = 3 
    while count <= num:
        fib_num = first + second
        first = second
        second = fib_num
        count += 1

    return fib_num

print(fib(num))

