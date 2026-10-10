import random
import time
import sys
import builtins
import os
import nltk

nltk.download('words')
from nltk.corpus import words
word_list = words.words()

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
def memory_game():
    global willow
    n_list = []
    correct_numbers = 0
    type_scroll("I'll flash 10 numbers in front of you, and you'll have to remember them in order.")
    type_scroll("Get all 10 and you win 20 willow.")
    type_scroll("Get 7-9 in their correct positions and you win 5 willow.")
    type_scroll("Get 6 or less and you lose 10 willow.")
    time.sleep(0.5)
    input("Press Enter to start the game.")
    for i in range(10):
        number = random.randint(1, 99)
        print(number)
        n_list.append(number)
        time.sleep(0.75)
        clear_screen()
        time.sleep(0.75)
    type_scroll("That's 10 of them!")
    for i in range(10):
        guess = intinput(f"Now, enter the number you saw in position {i+1}: ")
        if n_list[i] == guess:
            type_scroll("Correct!")
            correct_numbers += 1
        else: 
            type_scroll(f"Wrong! It was {n_list[i]}.")
    if correct_numbers == 10:
        type_scroll("You got all 10! You win 20 willow...")
        willow += 20
        type_scroll("...I guess I agreed to that. I don't know why, but I did.")
        type_scroll("Good job, I guess. You have a good memory...")
    elif correct_numbers >= 8:
        type_scroll(f"You got {correct_numbers} correct. You win 10 willow.")
        willow += 10
        type_scroll("Hmmm, you won quite a bit... Good for you, I guess?")
    elif correct_numbers >= 5:
        type_scroll(f"You got {correct_numbers} correct. You win 5 willow.")
        willow += 5
        type_scroll("Well, you won something. Good for you.")
    else:
        type_scroll(f"Woo! You only got {correct_numbers} correct. I get 10 willow!")
        willow -= 10
        type_scroll("Thanks! That was tasty. I love willow.")
def hangman():
    global willow
    type_scroll("Hangman, huh?")
    type_scroll("You have to guess the word I'm thinking of, letter by letter.")
    type_scroll("A guess is either a letter or the whole word. ")
    type_scroll("If you guess the whole word and get it wrong, you lose instantly.")
    type_scroll("I'll give you the length of the word.")
    type_scroll("Get it in 5 or less guesses and you win 20 willow.")
    type_scroll("Get it in 6-7 guesses and you win 5 willow.")
    type_scroll("Get it in 8-10 guesses and you lose 5 willow.")
    type_scroll("If it takes you more than 10 guesses or you guess the wrong word, you lose 10 willow.")
    word = random.choice(word_list)
    correct_layout = list(word)
    word_length = len(word)
    guesses = 0
    word_layout = []
    guessed_letters = []
    for i in range(word_length):
        word_layout.append("_")
    type_scroll("Are you ready? Press Enter to start.")
    input()
    type_scroll(f"The word is {word_length} letters long.")
    print(" ".join(word_layout))

    while 1:
        letter = input("Guess a letter or the whole word: ")
        guesses += 1
        if len(letter) > 1:
            if letter == word:
                type_scroll("That's the word!")
                if guesses <= 5:
                    type_scroll(f"It only took you {guesses} guesses. Wow. You win 20 willow... ")
                    willow += 20
                elif guesses < 8:
                    type_scroll(f"It took you {guesses} guesses. You win 5 willow.")
                    willow += 5
                elif guesses < 11:
                    type_scroll(f"It took you {guesses} guesses! Great, I get 5 willow!")
                    willow -= 5
                else:
                    type_scroll(f"But it took you {guesses} guesses! I get 10 willow!!!")
                    willow -= 10
                break
            else:
                type_scroll("Nope! That's not the word. Ha!")
                type_scroll(f"The word was {word}.")
                type_scroll("I get 10 willow for that. Thanks!")
                willow -= 10
                break
        if letter in correct_layout:
            type_scroll("Nice!")
            for i in range(word_length):
                if letter == correct_layout[i]:
                    word_layout[i] = letter
            print(" ".join(word_layout))
        else:
            guessed_letters.append(letter)
            try:
                int(letter)
                type_scroll("Hey, that's a number! Not a letter!")
                type_scroll("Although, I'm not complaining, it still counts as a guess.")
            except ValueError:
                type_scroll("Nope! That's not in the word.")
        type_scroll(f"That was guess #{guesses}.")
        type_scroll(f"These are your failed guesses: {guessed_letters}")

def intro():
    global willow
    clear_screen()
    type_scroll("Welcome to my cabin, agent.")
    type_scroll("Finally a visitor! I've been pretty bored lately.")
    type_scroll("You can call me moosespy.")
    type_scroll("You are most likely here to play some small minigames.")
    type_scroll("If you're not, then too bad, because I don't have much else to do.")
    type_scroll("Now, I love willow. Willow is my favorite food. If you wish to play, you must have some willow available.")
    type_scroll("Here's 50 willow. I'm feeling generous.")
    willow = 50
    type_scroll("I'm bored, so I'll let you play some games with me.")
    type_scroll("Lose all that willow back to me and I'll be bored again, so I'll kick you out. Game over.")
    type_scroll("So try to win as much willow as you can!")
def ending():
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

intro()
while 1:
    time.sleep(1)
    while 1:
        type_scroll("You can either: ")
        type_scroll("1) Play a game with me.")
        type_scroll("2) Check your statistics.")
        type_scroll("3) Enter save code.")
        type_scroll("4) Save game and exit.")
        play_game = input("So what do you want to do (input # choice)? ")
        if play_game == "1":
            clear_screen()
            break
        elif play_game == "2":
            clear_screen()
            type_scroll("Your statistics are: ")
            type_scroll(f"Games played: {games_played}")
            type_scroll(f"Willow remaining: {willow}")
            print()
            type_scroll("Now then...")
        elif play_game == "3":
            clear_screen()
            save_code = input("Please input your save code: ")
            if save_code.startswith("moose") and save_code.endswith("spy"):
                try:
                    sub = save_code[5:]
                    willow2 = sub.split("abc")[0]
                    willow2 = int(willow2)
                    try:
                        games_played2 = sub.split("abc")[1]
                        games_played2 = games_played2.split("spy")[0]
                        games_played2 = int(games_played2/1000)
                        willow = willow2
                        games_played = games_played2
                        type_scroll(f"Save code accepted. You now have {willow} willow.")
                    except ValueError:
                        type_scroll("Invalid save code.")
                except ValueError:
                    type_scroll("Invalid save code.")
            else:
                type_scroll("Invalid save code.")
            print()
        elif play_game == "4":
            clear_screen()
            save_code = f"moose{willow}abc{(games_played * 1000)}spy"
            type_scroll("Saving game...")
            time.sleep(1)
            type_scroll(f"Your save code is: {save_code}")
            sys.exit()
        else:
            type_scroll("Come on, sir, just say one of the numbers. It's not that hard.")
    type_scroll("Let's play a game!")
    type_scroll("Our games are: ")
    print("1) Number Guesser")
    print("2) Antler Cup")
    print("3) Memory Game")
    print("4) Hangman")
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
        elif game == 3:
            clear_screen()
            memory_game()
            games_played += 1
            break
        elif game == 4:
            clear_screen()
            hangman()
            games_played += 1
            break
        else:
            game = intinput("Not a valid game, sir. Please input the number of the game you wish to play: ")
    type_scroll(f"You have {willow} willow.")
    if willow <= 0:
        ending()