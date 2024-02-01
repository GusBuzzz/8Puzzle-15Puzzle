# Puzzle Games: 8-Puzzle and 15-Puzzle

## 8-Puzzle

The 8-Puzzle is a sliding puzzle game with a 3x3 grid. The goal is to arrange the tiles in ascending order, with the empty tile in the bottom-right corner. You can move tiles into the empty space to rearrange them.

### Implementation Details

- The game is implemented using the A* algorithm with a heuristic function based on the Manhattan distance.
- The PuzzleNode class represents each state in the game, and the solve_8_puzzle function finds the shortest path to the goal state.

### Example Usage

```python
python 8Puzzle.py
```

## 15-Puzzle

The 15-Puzzle is a sliding puzzle game with a 4x4 grid. The goal is to arrange the tiles in ascending order, with the empty tile in the bottom-right corner. You can move tiles into the empty space to rearrange them.

### Implementation Details

- The game checks if the initial state is solvable using the parity of the permutation of tiles and the taxicab distance between the empty tile and the bottom-right corner.
- The Puzzle class represents each state in the game, and the solve function uses the A* algorithm to find the shortest path to the goal state.

### Example Usage

```python
python 15Puzzle.py
```

## Running the Games

1. Clone the repository to your local machine.
2. Navigate to the directory containing the Python files.
3. Run the desired game script:

   For 8-Puzzle:

   ```bash
   python 8Puzzle.py
   ```

   For 15-Puzzle:

   ```bash
   python 15Puzzle.py
   ```

Follow the on-screen instructions to observe the solution path or check if the puzzle is solvable.
