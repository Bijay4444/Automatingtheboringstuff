import random

print("Hello, What is your name? ")
name = input()

print(f'Well {name} think of a number between 1-20')
secretNumber = random.randint(1, 20)

for guessTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print("too low my friend")

    elif guess > secretNumber:
        print("too high my friend")

    else:
        break

if guess == secretNumber:
    print(f"Good job,{name} you guessd my number in {guessTaken}")
else:
    print(f"Nope. The number I was thinking of was {secretNumber}!")

print('Your took'+ str(guessTaken) + 'guesses.')