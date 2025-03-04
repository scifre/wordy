import multiprocessing
from numpy import average
from wordle import check_word, print_word, EXACT
from solver import possible_matches, calculate_entropy, best_first_guess
from copy import deepcopy
from pathlib import Path
import time


def next_guess(entropies):
    guess = ''
    max_entropy = -1
    for thing in entropies:
        if entropies[thing] > max_entropy:
            guess = thing
            max_entropy = entropies[thing]
    return guess


def cal(index_range, stats, times, answers, words, wordsize, lock):
    for index in range(*index_range):
        start = time.time()
        choice = answers[index]
        print(f"Answer: {choice}--{index}")
        words_copy = deepcopy(words)
        guesses = wordsize + 1

        guess, _ = best_first_guess(wordsize)
        previous_guess = set()
        previous_guess.add(guess)
        for i in range(0, guesses):
            status = [0] * wordsize
            score = check_word(guess, status, choice)

            print(f"Computer Guess {i + 1} : ", end="")
            print_word(guess, status)
            if score == (EXACT * wordsize):
                with lock:
                    stats[i + 1] += 1
                    print(stats)
                break

            print()
            words_copy = possible_matches(guess, status, words_copy, previous_guess)
            entropies = dict()
            for word in words_copy:
                entropies[word] = calculate_entropy(word, words_copy, wordsize)
            guess = next_guess(entropies)
            previous_guess.add(guess)
        stop = time.time()
        with lock:
            times.append(stop - start)


def get_stats(index_range, stats, times, answers, words, wordsize, lock):
    for index in range(*index_range):
        start = time.time()
        choice = answers[index]
        words_copy = deepcopy(words)
        guesses = wordsize + 1

        guess, _ = best_first_guess(wordsize)
        previous_guess = set()
        previous_guess.add(guess)
        for i in range(0, guesses):
            status = [0] * wordsize
            score = check_word(guess, status, choice)

            if score == (EXACT * wordsize):
                with lock:
                    stats[i + 1] += 1
                break

            words_copy = possible_matches(guess, status, words_copy, previous_guess)
            entropies = dict()
            for word in words_copy:
                entropies[word] = calculate_entropy(word, words_copy, wordsize)
            guess = next_guess(entropies)
            previous_guess.add(guess)
        stop = time.time()
        with lock:
            times.append(stop - start)


def simulate(wordsize: int, index_ranges, target):
    file_path_answers = Path(f"../words/answers/{wordsize}.txt")

    with open(file_path_answers) as file:
        answers = file.readlines()
        answers = [word.replace('\n', '').strip() for word in answers]

    file_path_allowed = Path(f"../words/answers/{wordsize}.txt")
    with open(file_path_allowed) as file:
        words = file.readlines()
        words = [word.replace('\n', '').strip() for word in words]

    ms = time.time()
    with multiprocessing.Manager() as manager:
        stats = manager.dict({(i+1): 0 for i in range(wordsize+1)})
        times = manager.list()
        lock = manager.Lock()

        processes = []

        for index_range in index_ranges:
            process = multiprocessing.Process(target=target, args=(index_range, stats, times, answers, words, wordsize, lock))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        print(f"Average Time Taken: {average(times):.3f}")
        # Average number of guesses
        num = 0
        sums = 0
        for k in stats.keys():
            sums += int(k * stats[k])
            num += int(stats[k])
        print(f"Average Number of guesses: {(sums / num):.3f}")
        ma = time.time()
        print(f"total time: {(ma-ms):.3f}")


if __name__ == "__main__":
    simulate(5)
