### **How the Witty Number Guessing Game Works:**

1. **Welcoming the Player**:  
   The game starts with a playful introduction, setting the tone for a fun guessing adventure. The program warns the player to be ready for some humorous feedback.
2. **Generating the Number**:  
   As before, the program generates a random number between 1 and 100 using the `random.randint(1, 100)` function.
3. **The Guessing Loop**:  
   In this loop, the player enters their guess, and the program responds with cheeky hints:
   - If the guess is **too low**, it suggests aiming higher with the message: `"Hmm... too low! Aim higher. 🚀"`
   - If the guess is **too high**, the game lightens the moment by saying: `"Whoa there! That's too high. Come back down to Earth. 🌍"`
   - When the player guesses correctly, they’re congratulated with a fun, celebratory message: `"Bravo! You've cracked the code in {guess_count} tries. 🏆"`
4. **Handling Invalid Input**:  
   If the player enters something that isn’t a number, the program catches the error and responds humorously: `"Really? That's not even a number! Try again. 🙄"`

````
Welcome to the Number Guessing Game!
I've picked a random number between 1 and 100. Your mission, should you choose to accept it, is to guess it.
But beware... I'll be watching your every move. 😈

Take a wild guess: 50
Hmm... too low! Aim higher. 🚀

Take a wild guess: 75
Whoa there! That's too high. Come back down to Earth. 🌍

Take a wild guess: 63
Bravo! You've cracked the code in 3 tries. 🏆
```
````
