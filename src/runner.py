import argparse
from wordle import play
from solver import best_first_guess, solve
from user_v_comp import compete
from test_solver_multiprocessing import simulate, cal, get_stats

parser = argparse.ArgumentParser(
    description="Play and Solve wordle games"
)

group = parser.add_mutually_exclusive_group()

# Play
group.add_argument(
    "-p",
    "--play",
    help="Play wordle with p letters",
    type=int,
    choices=[5, 6, 7]
)

# Compete
group.add_argument(
    "-c",
    "--compete",
    help="Compete against the solver in a game of c letters",
    type=int,
    choices=[5, 6, 7]
)

# Best First Guess
group.add_argument(
    "-f",
    "--first",
    help="Best first guesses & their entropies",
    type=int,
    choices=[5, 6, 7]
)

# Stats
group.add_argument(
    "-s",
    "--stats",
    help="Stats related to the solver",
    type=int,
    choices=[5, 6, 7]
)

# Simulate
group.add_argument(
    "-r",
    "--run",
    help="Runs the solver on a 100 random words",
    type=int,
    choices=[5, 6, 7]
)

# guess
group.add_argument(
    "-g",
    "--guess",
    help="Give a 5, 6, 7 letter word to guess",
    type=str
)

args = parser.parse_args()

if args.play:
    play(args.play)
elif args.first:
    word, entropy = best_first_guess(args.first)
    print(f"Best Possible word: {word}")
    print(f"Entropy: {entropy}")
elif args.compete:
    compete(args.compete)
elif args.stats:
    print("Generating...")
    if args.stats == 6:
        simulate(args.stats, [(1, 10), (100, 200), (200, 300), (300, 400)], target=get_stats)
    elif args.stats == 5:
        simulate(args.stats, [(1, 25), (25, 50), (50, 75), (75, 100)], target=get_stats)
    elif args.stats == 7:
        simulate(args.stats, [(1, 100), (100, 200), (200, 300), (300, 400)], target=get_stats)
elif args.run:
    simulate(args.run, [(1, 25), (25, 50), (50, 75), (75, 100)], target=cal)
elif args.guess:
    solve(args.guess)
