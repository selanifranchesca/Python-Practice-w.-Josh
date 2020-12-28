a = [5, 10, 15, 20, 25]

def firstandlast(numbers):
    global new_list
    new_list.append(numbers[0])
    new_list.append(numbers[len(numbers)-1])

new_list = []
firstandlast(a)

for a in new_list:
    print(str(a))
