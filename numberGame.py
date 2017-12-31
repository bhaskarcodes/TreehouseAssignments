import random

secret_number = random.randint(1, 10)
count_tries = 0
while True:
    guess = int(input("Guess a number between 1 and 10 : "))
    if (guess==secret_number):
        print("Bingo! We think alike")
        break
    elif count_tries<1:
        print("Nope! Try again!")
        count_tries +=1
    else:
        print("Game over ! I had thought of",secret_number)
        break
