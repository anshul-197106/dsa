import random
number = random.randint(1, 10)
chances = 3

while chances > 0:
    guess = int(input("Guess the number (1-10): "))
    if guess == number:
        print("You guessed it right!")
        break
    else:
        chances -= 1
        if chances == 0:
            print("Game Over! The number was", number)
        else:
            print("Wrong guess. Chances left:", chances)
