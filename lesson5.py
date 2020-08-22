a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# print([number for number in set(a) if number in set(b)])



def compare (a,b):
    c = []
    for numberinb in b:
        for numberina in a:
            if numberinb == numberina and numberinb not in c:
                c.append(numberinb)

    return c 

print(compare(a,b))

e = [1, 4, 7, 8, 12, 13, 15, 18, 23]
f = [1, 3, 7, 9, 13, 15, 16, 19, 23, 44]

print(compare(e,f))

def compareusingsets(a, b):
    return a & b

print(compareusingsets(set(a), set(b)))