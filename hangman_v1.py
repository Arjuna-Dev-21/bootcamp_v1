import random

# Starter word list
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist).lower()

# Set of guessed letters
guessed_letters = set()

# Body parts for hangman
hangman_parts = ['head', 'body', 'left arm', 'right arm', 'left leg', 'right leg']
wrong_guesses = 0
max_wrong_guesses = len(hangman_parts)

# Display with * for letters and space for spaces
display_word = ['*' if ch != ' ' else ' ' for ch in word]

def show_display():
    print("\nCurrent word: " + ''.join(display_word))
    print(f"Wrong guesses: {wrong_guesses}/{max_wrong_guesses}")
    print("Guessed letters:", ', '.join(sorted(guessed_letters)))

# Game loop
while True:
    show_display()
    guess = input("Guess a letter: ").lower()

    # Check for valid input
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("You have already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        for i, ch in enumerate(word):
            if ch == guess:
                display_word[i] = guess
        if '*' not in display_word:
            show_display()
            print("\nCongratulations! You guessed the word correctly!")
            break
    else:
        wrong_guesses += 1
        print(f"Wrong guess! {hangman_parts[wrong_guesses - 1]} added.")
        if wrong_guesses == max_wrong_guesses:
            print("\nYou've been hanged!")
            print(f"The word was: {word}")
            break
