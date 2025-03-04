import json
from solver import calculate_entropy


"""
Calculate entropies for all five letter words.
"""
def main():
    entropies = dict()

    with open('path.txt') as file:
        path = file.readline()
        
    path_allowed = path + f"/wordy/words/allowed/allowed_5_letter.txt"

    with open(path_allowed) as file:
        words = file.readlines()

    words = [word.replace('\n', '') for word in words]

    for word, entropy in calculate_entropies(words):
        entropies[word] = entropy
        print(f"{word}: {entropy}")
        with open('entropies.json', 'w') as file:
            json.dump(entropies, file)
    
def calculate_entropies(words):
    for word in words:
        yield word, calculate_entropy(word, words)
    
if __name__ == "__main__":
    main()