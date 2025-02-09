# CS170-Project-1-Eight-Puzzle

## File Output

The program writes the output to a file called `output.txt` in the same directory as the script. It includes the details of the search process, such as the states visited and the final result.

## Code Explanation

### Classes:
- **Node**: Represents a node in the search tree with a state, parent node, and children.
- **Tree**: Represents the search tree.
- **OutputFile**: Handles writing output to both the console and a file.

### Functions:
- **puzzle_children(state)**: Generates the possible states from the current puzzle state.
- **misplaced_tiles(puzzle)**: Heuristic function that calculates the number of misplaced tiles.
- **manhattan_distance(puzzle)**: Heuristic function that calculates the Manhattan distance.
- **uniform_cost_search(puzzle)**: Implements the Uniform Cost Search algorithm.
- **a_star_misplaced_heuristic(puzzle)**: Implements A* search using the Misplaced Tile Heuristic.
- **a_star_manhattan_heuristic(puzzle)**: Implements A* search using the Manhattan Distance Heuristic.
- **log_print(*args, **kwargs)**: Logs messages to both the console and the output file.

## Test Cases

The test cases are predefined puzzle configurations with varying depths from 0 to 24. They are used to test the different algorithms for solving the puzzle.

## Requirements

- Python 3.x


## Example Code

This Python program solves the 8 tile puzzle using three different search algorithms:
1. **Uniform Cost Search**
2. **A* with the Misplaced Tile Heuristic**
3. **A* with the Manhattan Distance Heuristic**

The program allows the user to choose from predefined test cases or input their own puzzle configuration. It will then solve the puzzle using one of the three algorithms and provide details such as the number of nodes expanded, the maximum number of nodes in the queue at any one time, and the depth of the goal node.

### Features

- **Uniform Cost Search**: Finds the goal state by expanding nodes based on the least cost (depth).
- **A* with Misplaced Tile Heuristic**: Uses the number of misplaced tiles as the heuristic to guide the search.
- **A* with Manhattan Distance Heuristic**: Uses the Manhattan distance between the tiles and their goal positions as the heuristic.

### Step 1: Choose Puzzle Type

Upon starting the program, you will be prompted to choose a puzzle:
- **1**: Use a default test-case puzzle.
- **2**: Input your own puzzle.

### Step 2: Choose Test Case (if applicable)

If you choose option **1**, you can select from the following test cases:

- **Depth 0**: Puzzle already in goal state.
- **Depth 2**: Puzzle with a depth of 2.
- **Depth 4**: Puzzle with a depth of 4.
- **Depth 8**: Puzzle with a depth of 8.
- **Depth 12**: Puzzle with a depth of 12.
- **Depth 16**: Puzzle with a depth of 16.
- **Depth 20**: Puzzle with a depth of 20.
- **Depth 24**: Puzzle with a depth of 24.

### Step 3: Choose Algorithm

After selecting the puzzle, you will be prompted to choose one of the following algorithms:
- **1**: Uniform Cost Search
- **2**: A* with the Misplaced Tile Heuristic
- **3**: A* with the Manhattan Distance Heuristic

### Step 4: Program Output

The program will output:
- The search algorithm’s progress at each step.
- The number of nodes expanded during the search.
- The maximum size of the queue during the search.
- The depth of the goal node.
- The time taken to complete the algorithm.

## Example

```text
--------------------------------------------------------------------------------
Welcome to 8 Tile Puzzle Solver.

Type '1' to use a default puzzle, or '2' to enter your own puzzle.
1
Choose a default (test-case) puzzle to solve:
     1: Depth 0
     2: Depth 2
     3: Depth 4
     4: Depth 8
     5: Depth 12
     6: Depth 16
     7: Depth 20
     8: Depth 24
2
Enter your choice of algorithm
   1: Uniform Cost Search
   2: A* with the Misplaced Tile Heuristic
   3: A* with the Manhattan Distance Heuristic
3
A* with the Manhattan Distance Heuristic:
Step 1:
The best state to expand with g(n) = 0 and h(n) = 4 is ...
1 2 3
4 0 5
6 7 8
-----
Step 2:
The best state to expand with g(n) = 1 and h(n) = 3 is ...
1 2 3
0 4 5
6 7 8
...
