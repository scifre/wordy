import math
from itertools import product
from copy import deepcopy


def calculate_entropy(word: str, possible_words: [str]):
    """
    (entropy) E[information] = Summation(p(x)*information)
    This functions calculates the entropy { E[information] } for a given word.
    Rounded to two decimal places.
    """
    sum = 0
    possible_status = list(product([0, 1, 2], repeat=5))
    for status in possible_status:
        probability = calculate_probability(word, list(status), possible_words)
        info = calculate_info_with_probability(probability)
        sum += (probability*info)
    return round(sum, 2)


def calculate_info_with_probability(probability: float):
    """
    information = -(log2(p(x))) { negative of log base 2 of probability of x }
    Calculates information { in terms of bits } for a given word.
    """
    if probability > 0:
        return -(math.log(probability, 2))
    else:
        return 0
    
def calculate_probability(guess: str, status: [int], possible_words: [str]):
    """
    (probability) p = Number of words (with same status) / possible_words
    Rounded to 4 decimal places.
    """
    return round((len(possible_matches(guess, status, possible_words))/ len(possible_words)), 4)


def possible_matches(guess: str, status: [int], possible_words: [str]):
    new_possible_words = []
    letters_not_in_word = []
    letters_at_correct_location = dict()
    letters_at_incorrect_location = dict()
    
    for i, letter in enumerate(guess):
        if status[i] == 0:
            letters_not_in_word.append(letter)
        elif status[i] == 1:
            letters_at_incorrect_location[letter] = i
        elif status[i] == 2:
            letters_at_correct_location[i] = letter
    
    for word in possible_words:
        match = False
        for i, letter in enumerate(word):
            if letter in letters_not_in_word:
                match = False
                break
            elif i in letters_at_correct_location:
                if letter != letters_at_correct_location[i]: 
                    match = False
                    break
                else:
                    match = True
            elif letter in letters_at_incorrect_location:
                if i != letters_at_incorrect_location[letter]:
                    match = True
                else:
                    match = False
                    break
            else:
                match = True
        for letter in letters_at_incorrect_location:
            if letter not in word:
                match = False
                break
        
        if match:
            new_possible_words.append(word)
    
    return new_possible_words