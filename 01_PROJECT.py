import random

while True:
    try:
        G = int(input("Enter the number of games: "))
        break
    except ValueError:
        print("Please enter a number")

A = 1
for i in range(G):
    R = random.randint(1, 25)
    while True:
        try:
            N = int(input("Enter a number between 1 to 25: "))
            if N > R:
                print("Too high")
                A += 1
            elif N < R:
                print("Too low")
                A += 1
            else:
                print("Guessed it right")
                print("Oops you took {} Attempts to clear the game".format(A))
                A = 1
                R = random.randint(1, 25)
                break
        except ValueError:
            print("Please enter a number")
