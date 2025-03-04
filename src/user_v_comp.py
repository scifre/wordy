import random
from wordle import check_word, print_word, EXACT, get_guess
from solver import possible_matches, calculate_entropy, best_first_guess
from copy import deepcopy
from termcolor import cprint
from pathlib import Path


def next_guess(entropies):
    guess = ''
    max_entropy = -1
    for thing in entropies:
        if entropies[thing] > max_entropy:
            guess = thing
            max_entropy = entropies[thing]
    return guess


def compete(wordsize: int):
    file_path_answers = Path(f"../words/answers/{wordsize}.txt")

    with open(file_path_answers) as file:
        answers = file.readlines()
        answers = [word.replace('\n', '').strip() for word in answers]

    file_path_allowed = Path(f"../words/answers/{wordsize}.txt")
    with open(file_path_allowed) as file:
        words = file.readlines()
        words = [word.replace('\n', '').strip() for word in words]

    choice = random.choice(answers)
    words_copy = deepcopy(words)
    guesses = wordsize + 1
    won = False
    comp_won = False
    cprint(f"{wordsize} letter - WORDLE", "green")
    cprint(f"You have {guesses} tries to guess the {wordsize}-letter word\n\n")
    guess, _ = best_first_guess(wordsize)
    previous_guess = set()
    previous_guess.add(guess)
    for i in range(0, guesses):
        user_guess = get_guess(words)
        user_status = [0]*wordsize
        user_score = check_word(user_guess, user_status, choice)
        status = [0] * wordsize
        score = check_word(guess, status, choice)
        print('\033[F', '\033[K' f"\rUser Guess {i + 1} : ", end='')
        print_word(user_guess, user_status)
        if user_score == (EXACT * wordsize):
            won = True
            break
        print(f"Computer Guess {i + 1} : ", end="")
        print_word(guess, status)
        if score == (EXACT * wordsize):
            comp_won = True
            break
        print()
        words_copy = possible_matches(guess, status, words_copy, previous_guess)
        entropies = dict()
        for word in words_copy:
            entropies[word] = calculate_entropy(word, words_copy, wordsize)
        guess = next_guess(entropies)
        previous_guess.add(guess)

    if won:
        print("\nCongratulation!, You Won")
    elif comp_won:
        print("\nComputer Won, better luck next time!")
    else:
        print("\nSorry, Both failed")


if __name__ == "__main__":
    compete()
