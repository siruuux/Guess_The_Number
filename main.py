import random
import time


print("----------WELCOME----------")
time.sleep(.5)
print("This is Guess the Number.")
time.sleep(.5)
number = random.randint(1, int(input("What should be the highest number you can guess?: ")))            # Here the player can choose the highest number (You can also delete everything after , and place any number you like
time.sleep(.5)
username = input("What is your name?: ")
time.sleep(.5)
print("Alright, let's type your guesses!!")
guess_count = 0



while guess_count < 5:          # 5 stands for the maximum tries you can do. If you want to you can go lower or higher
    guess = int(input())
    guess_count += 1            # This is the counter for your guesses. Always you input your guess, the guess_count will go up by 1
    if guess > number:
        print("Your guess is too high, go down")            # self-explanatory i guess

    if guess < number:
        print("Your guess is too low, go up")           # self-explanatory i guess

    if guess == number:         # self-explanatory i guess
        break

if guess == number:
    print("Perfect! ",username, " guessed the right number within ", guess_count, " guesses")
    print("The number was ", number)

else:
    print("You didn't guessed the right number. The right number was ", number)