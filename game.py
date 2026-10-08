import random

print("Let's play")
number = random.randint(1, 100)
attempt = 0
while 1:
    try:
        guess = int(input("guess number"))
        attempt += 1
        if guess == number:
            print("you win")
            break
        elif guess > number:
            print("lower")
        elif guess < number:
            print("higher")
    except ValueError:
        print("hey enter actual whole valid numbers")

print(f"you took {attempt} tries")