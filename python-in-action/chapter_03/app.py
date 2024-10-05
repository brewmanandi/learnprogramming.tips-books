# Number Guessing Game - The Ultimate Challenge

import random

# Step 1: Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Step 2: Introduce the game with a little flair
print("Welcome to the Number Guessing Game!")
print("I've picked a random number between 1 and 100. Your mission, should you choose to accept it, is to guess it.")
print("But beware... I'll be watching your every move. 😈")

# Step 3: Keep track of the number of guesses
guess_count = 0

# Step 4: Begin the guessing loop - let the mind games begin
while True:
    try:
        guess = int(input("\nTake a wild guess: "))
        guess_count += 1  # Increase guess count with every guess

        if guess < number_to_guess:
            print("Hmm... too low! Aim higher. 🚀")
        elif guess > number_to_guess:
            print("Whoa there! That's too high. Come back down to Earth. 🌍")
        else:
            print(f"🎉 Bravo! You've cracked the code in {guess_count} tries. 🏆")
            break

    except ValueError:
        print("Really? That's not even a number! Try again. 🙄")
