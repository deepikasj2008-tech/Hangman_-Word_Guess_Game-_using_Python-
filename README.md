# Hangman_-Word_Guess_Game-_using_Python-

The Hangman Game is a simple Python-based word guessing game where the player tries to guess a hidden word letter by letter.

At the start, the program randomly selects a word from a predefined list such as apple, banana, grape, mango, and orange. The selected word is hidden using underscores (_), and the player must guess the correct letters within a limited number of attempts (6 chances).

🔹 How it works:
The player enters one letter at a time.
If the guessed letter is correct, it is revealed in the correct position(s) of the word.
If the guessed letter is wrong, the number of attempts decreases.
The game also checks if the letter was already guessed to avoid repetition.
🔹 Game Outcomes:
🎉 Win: When the player correctly guesses all letters before attempts run out.
❌ Lose: When all attempts are used and the word is still incomplete.
🔹 Concepts Used:
Random module (random.choice)
Lists (to store words and guessed letters)
Loops (while)
Conditional statements (if-else)
String handling
