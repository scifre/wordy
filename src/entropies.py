import json
from solver import calculate_entropy
import sys
from pathlib import Path

"""
Calculate entropies for all n letter words.
"""


def main():
    entropies = dict()

    file_path_answers = Path(f"../words/answers/{sys.argv[1]}.txt")
    with open(file_path_answers) as file:
        words = file.readlines()
        words = [word.replace('\n', '').strip() for word in words]

    for word, entropy in calculate_entropies(words, int(sys.argv[1])):
        entropies[word] = entropy
        print(f"{word}: {entropy}")
        with open(f'entropies{sys.argv[1]}.json', 'w') as file:
            json.dump(entropies, file, indent=4)


def calculate_entropies(words, repeat=5):
    for word in words:
        yield word, calculate_entropy(word, words, repeat)


if __name__ == "__main__":
    main()
