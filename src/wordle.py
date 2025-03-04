import sys
from termcolor import cprint
import random
from pathlib import Path

EXACT = 2  # If letter in correct place
CLOSE = 1  # If letter not in correct place
# 0 If letter not in word


def play(wordsize: int):
    file_path_answers = Path(f'../words/answers/{wordsize}.txt')
    with open(file_path_answers) as file:
        words = file.readlines()
        words = [word.replace('\n', '') for word in words]

    choice = random.choice(words)
    guesses = wordsize + 1
    won = False
    cprint(f"{wordsize} letter - WORDLE", "green")
    cprint(f"You have {guesses} tries to guess the {wordsize}-letter word")

    file_path_possible = Path(f'../words/allowed/allowed_{wordsize}_letter.txt')

    with open(file_path_possible) as file:
        allowed_words = file.readlines()
        allowed_words = [word.replace('\n', '') for word in allowed_words]

    for i in range(0, guesses):
        guess = get_guess(allowed_words)
        status = [0] * wordsize
        score = check_word(guess, status, choice)
        print(f"Guess {i + 1} : ", end="")
        print_word(guess, status)
        if score == (EXACT * wordsize):
            won = True
            break

    if won:
        print("You won!")
    else:
        print(f"The correct word was : {choice}")


def main():
    if (len(sys.argv)) != 2:
        sys.exit("Usage: python wordle.py wordsize")
    else:
        try:
            wordsize = int(sys.argv[1])
        except TypeError:
            sys.exit("Wordsize should be an Integer")
        if wordsize < 5 or wordsize > 8:
            sys.exit("Error: wordsize must be either 5, 6, 7 or 8")

    play(wordsize)


def get_guess(allowed_words: [str]) -> str:
    """
    Continuously asks for input until a valid word is provided.
    """
    while True:
        guess = input("Enter your guess : ")
        if guess in allowed_words:
            return guess
        else:
            print("Please enter a valid word.")


def check_word(guess: str, status: [int], choice: str) -> int:
    """
    Updates the status list with the score of each letter: 0, CLOSE, EXACT.
    Score is returned which is used to check whether the guess is correct.
    """
    score = 0
    choice_info = create_word(choice)
    guess_info = create_word(guess)
    for letter in guess_info:
        if letter in choice_info:
            occurence_count = len(choice_info[letter])
            guess_count = len(guess_info[letter])
            for position in choice_info[letter]:
                if position in guess_info[letter]:
                    status[position] = EXACT
                    score += EXACT
                    occurence_count -= 1
                    guess_count -= 1
            if occurence_count > 0:
                for position in guess_info[letter]:
                    if status[position] != EXACT:
                        if occurence_count > 0 and guess_count > 0:
                            status[position] = CLOSE
                            occurence_count -= 1
                            guess_count -= 1
                            score += CLOSE
                        else:
                            break
    return score


def print_word(guess: str, status: [int]) -> None:
    """
    Used to colour print the guess according to the status.
    """
    for i, letter in enumerate(guess):
        if status[i] == EXACT:
            cprint(letter, "green", end="")
        elif status[i] == CLOSE:
            cprint(letter, "yellow", end="")
        else:
            print(letter, end="")
    print()


def create_word(word: str) -> dict:
    """
    Represents a word as a dictionary where the keys are the letters,
    the value is a list of the positions of the letter.
    """
    info = dict()
    for i, letter in enumerate(word):
        if letter in info:
            info[letter].append(i)
        else:
            info[letter] = [i]
    return info


if __name__ == "__main__":
    main()
