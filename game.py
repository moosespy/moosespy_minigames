import random
import time
import sys
import builtins
import os

games_played = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def type_scroll(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def intinput(question):
    while 1:
        user_input = input(question)
        try:
            integer_value = int(user_input)
            return(integer_value)
        except ValueError:
            type_scroll("Come on, enter a whole number.")

def randint_guess():
    global willow
    number = random.randint(1, 100)
    type_scroll("I'm thinking of a number between 1 and 100.")
    type_scroll("Get it under 5 guesses, you get 20 willow.")
    type_scroll("5-6 guesses, 0 willow.")
    type_scroll("7 guesses, pay 5 willow. ")
    type_scroll("More than 7? 10 willow paid to me.")
    attempt = 0
    while 1:
        try:
            guess = intinput("Guess the secret number: ")
            attempt += 1
            if guess == number:
                type_scroll("You guessed it!")
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

def antler_cup():
    global willow
    og_willow = willow
    streak = 0
    type_scroll("A part of my antler broke off once upon a time.")
    type_scroll("I've hidden it under cup 1, 2, or 3.")
    type_scroll("Just guess the cup and double the amount you put in!")
    while 1:
        while 1:
            bet = intinput("So how much willow would you like to put in? ")
            if bet > willow:
                type_scroll("Too much, sir, you'll end up in debt!")
                type_scroll(f"You know you only have {willow} willow, right?")
            else:
                break
        cup = random.randint(1, 3)
        type_scroll("Alright, I've hidden the antler chunk under one of the cups.")
        guess = intinput("So, then. What cup is my antler chunk under? ")
        if guess == cup:
            type_scroll(f"You got it. It was cup {cup}. You won {bet} willow.")
            if streak == 0:
                willow += bet
            else:
                willow += bet * streak
            type_scroll(f"You now have {willow} willow.")
            streak += 1
            type_scroll(f"Do you want to play again? You're on a streak of {streak}!")
            pag = input(f"Win this and you get {streak}x your bet! Lose and you lose everything! (y/n) ")
            if pag == "y":
                continue
            else:
                break
        else:
            if streak == 0:
                type_scroll(f"Wow, you lost your first bet. That's {bet} willow gone. It was cup {cup}.")
                willow = willow - bet
            else:
                type_scroll(f"Hah! Nope. It was cup {cup}! You just lost {bet * streak} willow!")
                willow = willow - (bet * streak)
            break
    type_scroll("Good game. Hope you liked it.") 
        
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
    time.sleep(1)
    while 1:
        type_scroll("You can either: ")
        type_scroll("1) Play a game with me.")
        type_scroll("2) Check your statistics.")
        play_game = input("So what do you want to do (input # choice)? ")
        if play_game == "1":
            clear_screen()
            break
        elif play_game == "2":
            clear_screen()
            type_scroll("Your statistics are: ")
            type_scroll(f"Games played: {games_played}")
            type_scroll(f"Willow remaining: {willow}")
            type_scroll("Now then...")
        else:
            type_scroll("Come on, sir, just say 1 or 2. It's not that hard.")
    type_scroll("Let's play a game!")
    type_scroll("Our games are: ")
    print("1) Number Guesser")
    print("2) Antler Cup")
    game = intinput("Please input the number of the game you wish to play: ")
    while 1:
        if game == 1:
            clear_screen()
            randint_guess()
            games_played += 1
            break
        elif game == 2:
            clear_screen()
            antler_cup()
            games_played += 1
            break
        else:
            game = intinput("Not a valid game, sir. Please input the number of the game you wish to play: ")
    type_scroll(f"You have {willow} willow.")
    if willow <= 0:
        type_scroll("So you ended up losing all your willow to me.")
        time.sleep(1)
        type_scroll("'sigh'... I'm bored again. Sadly, you'll be kicked out... ")
        time.sleep(1)
        type_scroll("...you're just not entertaining if you lose all your willow.")
        time.sleep(1)
        if games_played == 1:
            type_scroll(f"At least we got to play a game... but only 1...")
        else:
            type_scroll(f"At least we got to play {games_played} games.")
        time.sleep(1)
        type_scroll("Goodbye, agent.")
        sys.exit()