import random

# Predefined list of words
words = ["python", "hangman", "challenge", "programming", "code"]

def hangman():
    # Randomly select a word from the list
    word_to_guess = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        # Display the current state of the guessed word
        current_state = ''.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])
        print(f"Word: {current_state}")
        print(f"Guessed Letters: {', '.join(guessed_letters)}")
        print(f"Incorrect Guesses: {incorrect_guesses}/{max_incorrect_guesses}")

        # Get user input
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Incorrect guess!")
            incorrect_guesses += 1

        # Check if the player has won
        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"Congratulations! You've guessed the word: {word_to_guess}")
            break
    else:
        print(f"Game over! The correct word was: {word_to_guess}")

# Start the game
hangman()
