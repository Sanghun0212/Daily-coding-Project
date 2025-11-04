## Daily_Code_1

import random

secret = random.randint(1, 10)   ## int --> integar
                                 ## random.randint(a, b)
tries = 0

while True:

    guess = int(input("Enter a number: "))
    tries += 1

    if guess < secret:
        print("TOO Low!")
    
    elif guess > secret:
        print("TOO High!")

    else:
        print(f"Correct! you guessed {tries}tries!")
        break


print("Program finished!")