import random

#2 Word guessing Game in Python
# This program is a simple word-guessing game where the user has to guess the characters in a randomly
# selected word within a limited number of attempts.
# The program provides feedback after each guess, helping the user to either complete the word or lose the game based on their guesses.


words = ["cat", "mouse","dog","cow"]
word = random.choice(words)

guessed = ""
tries = 5

while tries > 0:
    for char in word:
        print(char if char in guessed else "_", end=" ")
    print()

    guess = input("Guess a letter: ")
    if guess in word:
        guessed += guess
    else:
        tries -= 1
        print("Wrong! Tries left:", tries)

    if all(char in guessed for char in word):
        print("You win! Word was:", word)
        break

if tries == 0:
    print("You lose! Word was:", word)