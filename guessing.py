import random

num = random.randint(1,20)
guess = None

while guess != num:
    guess = int(input("Guess a number between 1 to 20: "))

    if guess == num:
        print("Congrats! You won!!")
        break
    else:
        print("Oops! Wrong guess")
        #print("Right number is:{}".format(num))
        