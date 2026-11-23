# CodeAlpha Hangman Game

## Internship Task 1 — Python Programming

### Project overview
A simple text-based Hangman game built with Python. The computer selects one word randomly from a predefined list of five words. The player guesses one letter at a time and has a maximum of six incorrect guesses.

### Features
- Random selection from five predefined words
- One-letter-at-a-time guessing
- Six incorrect guesses allowed
- Input validation (rejects numbers, symbols, and multiple characters)
- Prevents the same letter from being guessed twice
- Displays the partially guessed word
- Announces win or game over

### Concepts used
`random`, lists, strings, sets, `while` loops, `if-else`, functions, user input, and basic validation.

### Requirements
- Python 3.8 or later
- No external libraries required

### How to run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python hangman.py
```

On some systems, use `python3 hangman.py`.

### Example gameplay
The selected word is random, so your output may differ.

```text
===== WELCOME TO HANGMAN =====
Guess the hidden word one letter at a time.
You can make 6 incorrect guesses.

Word: _ _ _ _ _ _
Incorrect guesses left: 6
Enter a letter: p
Correct guess!

Word: p _ _ _ _ _
Incorrect guesses left: 6
Enter a letter: y
Correct guess!

Word: p y _ _ _ _
Incorrect guesses left: 6
Enter a letter: t
Correct guess!

Word: p y t _ _ _
Incorrect guesses left: 6
Enter a letter: h
Correct guess!

Word: p y t h _ _
Incorrect guesses left: 6
Enter a letter: o
Correct guess!

Word: p y t h o _
Incorrect guesses left: 6
Enter a letter: n
Correct guess!

Word: p y t h o n
Congratulations! You guessed the word: python
YOU WIN!
```

### Project structure
```text
CodeAlpha_HangmanGame/
├── hangman.py
├── README.md
└── screenshots/
```

### Author
Python Programming Intern — CodeAlpha
