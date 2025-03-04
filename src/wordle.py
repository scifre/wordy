import sys
from termcolor import cprint
import random

EXACT = 2 # If letter in correct place
CLOSE = 1 # If letter not in correct place
# 0 If letter not in word


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
    
    with open("path.txt") as file:
        path = file.readline().strip()

    file_path_answers = path + f"/wordy/words/answers/{wordsize}.txt"    
    with open(file_path_answers) as file:
        words = file.readlines()    
        words = [word.replace('\n','') for word in words]

    choice = random.choice(words)
    guesses = wordsize + 1
    won = False
    cprint(f"{wordsize} letter - WORDLE", "green")
    cprint(f"You have {guesses} tries to guess the {wordsize}-letter word")

    file_path_possible = path + f"/wordy/words/allowed/allowed_{wordsize}_letter.txt"

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


def get_guess(allowed_words: [str]):
    """
    Continuously asks for input until a valid word is provided.
    """
    while True:
        guess = input("Enter your guess : ")
        if guess in allowed_words:
            return guess
        else:
            print("Please enter a valid word.")


def check_word(guess: str, status: [int], choice: str):
    """
    Updates the status list with the score of each letter: 0, CLOSE, EXACT.
    Score is returned which is used to check whether the guess is correct.
    """
    score = 0
    choice_info = create_word(choice) 
    guess_info = create_word(guess) 
    for letter in guess_info:
        found, correct_positions = find_letter(letter, choice_info)
        if found:
            correct_occurences = len(correct_positions) 
            for position in correct_positions:
                if position in letter.positions:
                    status[position] = EXACT
                    score += EXACT
                    correct_occurences -= 1
            if correct_occurences > 0:
                left_positions = letter.positions - correct_positions
                for position in left_positions:
                    if correct_occurences <= 0:
                        break
                    else:
                        status[position] = CLOSE
                        score += CLOSE
                        correct_occurences -= 1
    return score


def print_word(guess: str, status: [int]):
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


class Letter:
    """
    Each word is represented as an list of Letter Objects.
    This was done to better handle edge cases while assigning status to words with repeating letters.
    """
    def __init__(self, letter: str) -> None:
        self.letter = letter
        self.positions = set() 
    
    def __str__(self):
        return f"{self.letter} : {str(self.positions)}"


def create_word(word: [Letter]):
    """
    Represents the guess and correct answer as a list of Letter Class objects.
    """
    letters = []
    unique_letters = set(word)
    for letter in unique_letters:
        a_letter = Letter(letter)
        for i, each in enumerate(word):
            if each == letter:
                a_letter.positions.add(i)
        letters.append(a_letter)
    return letters 


def find_letter(letter: Letter, word: [Letter]):
    """
    letter: Letter Class object
    word: list of Letter Class objects
    returns True and all positions in the word of the letter.
    
    For example, 
        letter.letter = 'a'
        word = [a, d, e, f]
        a.positions = [1, 2]
        function returns [True, [1, 2]] 
    """
    for each in word:
        if letter.letter == each.letter:
            return True, each.positions
    return False, None


if __name__ == "__main__":
    main()