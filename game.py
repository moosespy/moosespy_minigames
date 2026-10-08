import random
import time
import sys
import builtins
def type_scroll(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def randint_guess():
    global willow
    number = random.randint(1, 100)
    type_scroll("Get it under 5 guesses, you get 20 willow.")
    type_scroll("5-6 guesses, 0 willow.")
    type_scroll("7 guesses, pay 5 willow. ")
    type_scroll("More than 7? 10 willow paid to me.")
    attempt = 0
    while 1:
        try:
            guess = int(input("Guess the secret number: "))
            attempt += 1
            if guess == number:
                type_scroll("you guessed it!")
                break
            elif guess > number:
                type_scroll("Lower")
            elif guess < number:
                type_scroll("Higher")
        except ValueError:
            type_scroll("Hey, enter actual whole valid numbers.")

    type_scroll(f"You took {attempt} tries.")
    if attempt > 7:
        type_scroll("That means you pay me 10 willow. Ouch.")
        willow -= 10
    elif attempt == 7:
        type_scroll("That means you pay me 5 willow. At least it's not more.")
        willow -= 5
    elif attempt < 7 and attempt > 4:
        type_scroll("That means you earn nothing. Too bad for you.")
    else:
        type_scroll("That means you win 20 willow... that's a bit much, but I guess I agreed...")
        willow += 20

type_scroll("Welcome to my cabin, agent.")
type_scroll("You can call me moosespy.")
type_scroll("You are most likely here to play some small minigames.")
type_scroll("Now, I love willow. Willow is my favorite food. If you wish to play, you must have some willow available.")
type_scroll("Here's 50 willow. I'm feeling generous.")
willow = 50
type_scroll("I'm bored, so I'll let you play some games with me.")
type_scroll("Lose all that willow back to me and I'll be bored again, so I'll kick you out. Game over.")
type_scroll("So try to win as much willow as you can!")
while 1:
    type_scroll("Let's play!")
    type_scroll("Our games are: ")
    print("1) Number Guesser")
    game = int(input("Please input the number of the game you wish to play: "))
    while 1:
        if game == 1:
            randint_guess()
            break
        else:
            game = int(input("Not a valid game, sir. Please input the number of the game you wish to play: "))
    type_scroll(f"You have {willow} willow.")