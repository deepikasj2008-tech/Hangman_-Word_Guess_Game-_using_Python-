import random 
words = ["apple", "banana", "grape", "mango", "orange"] 

word = random.choice(words) 

guessed_letters = [] 

attempts = 6 

print(" Welcome to Hangman Game!") 
display = ["_"] * len(word) 

while attempts > 0: 

    print("\nWord:", " ".join(display)) 

    guess = input("Enter a letter: ").lower() 

    if guess in guessed_letters: 

        print("️ You already guessed that letter!") 

        continue 

    guessed_letters.append(guess) 

    if guess in word: 

        print(" Correct!") 

        for i in range(len(word)): 

            if word[i] == guess: 

                display[i] = guess 

    else: 

        attempts -= 1 

        print(" Wrong! Attempts left:", attempts) 

    if "_" not in display:
        print(" You Win! The word is:", word) 

    break 

# If lost 

if "_" in display: 

    print(" You Lost! The word was:", word) 
