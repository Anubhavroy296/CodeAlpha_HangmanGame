import random

# Five predefined words for the game
WORDS = ["python", "computer", "program", "developer", "keyboard"]
MAX_INCORRECT_GUESSES = 6


def display_word(secret_word, guessed_letters):
    """Return the word with unguessed letters hidden as underscores."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in secret_word)


def play_game():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    incorrect_guesses = 0

    print("\n===== WELCOME TO HANGMAN =====")
    print("Guess the hidden word one letter at a time.")
    print(f"You can make {MAX_INCORRECT_GUESSES} incorrect guesses.\n")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print("Word:", display_word(secret_word, guessed_letters))
        print("Incorrect guesses left:", MAX_INCORRECT_GUESSES - incorrect_guesses)

        guess = input("Enter a letter: ").strip().lower()

        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetic letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.\n")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!\n")
            if all(letter in guessed_letters for letter in secret_word):
                print("Word:", display_word(secret_word, guessed_letters))
                print("Congratulations! You guessed the word:", secret_word)
                print("YOU WIN!")
                return
        else:
            incorrect_guesses += 1
            print("Wrong guess!\n")

    print("You have used all 6 incorrect guesses.")
    print("The correct word was:", secret_word)
    print("GAME OVER!")


if __name__ == "__main__":
    play_game()
