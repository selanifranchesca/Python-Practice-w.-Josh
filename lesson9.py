import random
a = random.randint(1,9)
count = 0

while(True):

    num = int(input("Guess a number between 1 and 9 or type 'exit' to leave the game."))
    if num == 'exit':
        break
    
    elif a == int(num):
        count += 1
        print("Thats correct! You guessed {} and the correct number is {}".format(num,a))
        break
    elif int(num) > a:
        count += 1
        print("Oops! You guess the number was {}. Try something smaller".format(num))
    else:
        count += 1
        print("Too low this time. You guessed {}, Try again.".format(num))

print('You have made {} guesses '.format(count))
print('The random number was {}'.format(a))
