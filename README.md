# Wordle Solver & Player

This is a command-line tool for playing and solving Wordle games. It includes multiple functionalities such as playing the game, competing against the solver, getting the best first guess, generating statistics, and running simulations.

## Features
- Play Wordle with 5, 6, or 7 letters.
- Compete against the solver.
- Get the best first guess based on entropy calculations.
- Generate statistics related to the solver.
- Run the solver on a set of random words.
- Solve a Wordle word by providing a guess.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/wordle-solver.git
   cd wordle-solver
   ```
2. Install dependencies (if any required):
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the program using Python and pass the appropriate command-line arguments:

### Playing Wordle
To play Wordle with a chosen word length (5, 6, or 7 letters):
```sh
python main.py --play 5
```

### Competing Against the Solver
To compete against the solver in a Wordle game:
```sh
python main.py --compete 6
```

### Finding the Best First Guess
To find the best first guess and its entropy:
```sh
python main.py --first 5
```

### Generating Solver Statistics
To generate statistics related to the solver:
```sh
python main.py --stats 7
```

### Running Solver Simulations
To run the solver on 100 random words:
```sh
python main.py --run 6
```

### Solving a Wordle Word
To get the best guesses for a specific word:
```sh
python main.py --guess "apple"
```

## Contributing
Feel free to submit issues or contribute by making pull requests.

## License
This project is licensed under the MIT License.

