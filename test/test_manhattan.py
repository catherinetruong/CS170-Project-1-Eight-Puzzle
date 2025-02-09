import queue
import time

#--------------------------------------------------------------
# global
goal_state = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 0]
            ]

#--------------------------------------------------------------

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
test_cases = {  "depth_0": [ #1
                            [1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 0],    
                        ],  
                "depth_2": [ #2
                            [1, 2, 3],
                            [4, 5, 6],
                            [0, 7, 8],    
                        ], 
                "depth_4": [ #3
                            [1, 2, 3],
                            [5, 0, 6],
                            [4, 7, 8],    
                        ], 
                "depth_8": [ #4
                            [1, 3, 6],
                            [5, 0, 2],
                            [4, 7, 8],    
                        ], 
                "depth_12": [ #5
                            [1, 3, 6],
                            [5, 0, 7],
                            [4, 8, 2],    
                        ], 
                "depth_16": [#6
                            [1, 6, 7],
                            [5, 0, 3],
                            [4, 8, 2],    
                        ], 
                "depth_20": [ #7
                            [7, 1, 2],
                            [4, 8, 5],
                            [6, 3, 0],    
                        ], 
                "depth_24": [ #8
                            [0, 7, 2],
                            [4, 6, 1],
                            [3, 5, 8],    
                        ],
              }

#--------------------------------------------------------------

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, state, parent=None):
        node = Node(state, parent)
        if parent is None:
            self.root = node
        else:
            parent.add_child(node)
        return node

#--------------------------------------------------------------   

# returns possible moves for 0 at current state board configuration
def puzzle_children(state):
    # keeps a list for the possible moves we can make
    next_states = []

    #              right   left    down     up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  

    # get the row & column index of the blank tile
    blank_row_pos = blank_row(state)
    blank_col_pos = blank_column(state)

    for direction in directions: #i.e. input 0,1
        # gets the first value in the list (row)
        new_row = blank_row_pos + direction[0]
        # gets the second value in the list (column)
        new_col = blank_col_pos + direction[1]

        # check for connections
        if 0 <= new_row and new_row < 3 and 0 <= new_col and new_col < 3:
            # makes a duplicate state of the passed in puzzle
            new_state = [list(row) for row in state]
            
            # swaps the two tiles
            temp = new_state[blank_row_pos][blank_col_pos]
            new_state[blank_row_pos][blank_col_pos] = new_state[new_row][new_col]
            new_state[new_row][new_col] = temp
            
            # added as one of the new states
            next_states.append(new_state)

    # returns the list of states that the puzzle could branch to            
    return next_states

# returns row position of 0        
def blank_row(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i
            
# returns column position of 0            
def blank_column(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return j
            
# testing function
def print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(map(str, row)))

def valid_puzzle(puzzle):
    # creates hashmap with keys 0-8 all with value 1 (in order to check if diff)
    valid_map = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1} 
    hashmap = {}
    for row in puzzle:
        for num in row:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
    
    # checks if hashmap and valid_map are equal
    equal_maps = True
    for key in valid_map:
        if key not in hashmap or hashmap[key] != valid_map[key]:
            equal_maps = False
            break
    
    return equal_maps

def print_tree_path(node):
    path = []
    while node is not None:
        path.append(node.state)
        node = node.parent

    print("Tree path from initial state to goal state:")
    for state in reversed(path):
        print_puzzle(state)
        print("-----")


#---------------------------------------------------------------------------------------------------
#v1
def a_star_manhattan_heuristic(puzzle):
    frontier = queue.PriorityQueue()  #initializes a priority queue where states (puzzzles pieces) are prioritized based on the depth of the node (g(n))
    visited = set()
    frontier.put((manhattan_distance(puzzle), 0, puzzle))  

    # counters
    max_pq_nodes = 0
    expanded_nodes = 0
    goal_depth = 0

    while not frontier.empty():
        manhattan, cost, curr_puzzle = frontier.get()
        visited.add(tuple(map(tuple, curr_puzzle)))
        step = cost + 1
        print("-----")
        print("Step " + str(step) + ":")
        print("The best state to expand with g(n) = " + str(cost) + " and h(n) = " + str(manhattan_distance(curr_puzzle)) + " is ...")
        print_puzzle(curr_puzzle)
        #print str(cost)
        if curr_puzzle == goal_state:
            return curr_puzzle, expanded_nodes, max_pq_nodes, goal_depth

        cost += 1
        expanded_nodes += 1
        goal_depth = max(goal_depth, cost)

        for child in puzzle_children(curr_puzzle):
            #if tuple(map(node, child)) not in visited:
            if tuple(map(tuple, child)) not in visited:
                frontier.put((manhattan_distance(child) + cost, cost, child))
                max_pq_nodes = max(max_pq_nodes, frontier.qsize())
    
    return None, expanded_nodes, max_pq_nodes, goal_depth  


#v2
def a_star_manhattan_heuristic(puzzle):
    start_time = time.time()  # start the timer
    frontier = queue.PriorityQueue()  #initializes a priority queue where states (puzzzles pieces) are prioritized based on the depth of the node (g(n))
    visited = set()
    frontier.put((manhattan_distance(puzzle), 0, puzzle))  

    # counters
    max_pq_nodes = 0
    expanded_nodes = 0
    goal_depth = 0

    while not frontier.empty():
        manhattan, cost, curr_puzzle = frontier.get()
        visited.add(tuple(map(tuple, curr_puzzle)))
        step = cost + 1
        print("-----")
        print("Step " + str(step) + ":")
        print("The best state to expand with g(n) = " + str(cost) + " and h(n) = " + str(manhattan_distance(curr_puzzle)) + " is ...")
        print_puzzle(curr_puzzle)

        if curr_puzzle == goal_state:
            end_time = time.time()  # end the timer if no solution found
            elapsed_time = round(end_time - start_time, 3)  # round to 3 decimal place, thousandths. if <=2 places, shows 0.0s
            print(f"Algorithm completed in {elapsed_time} seconds")

            return curr_puzzle, expanded_nodes, max_pq_nodes, goal_depth
        
        print("Expanding node above...")

        cost += 1
        expanded_nodes += 1
        goal_depth = max(goal_depth, cost)

        for child in puzzle_children(curr_puzzle):
            if tuple(map(tuple, child)) not in visited:
                frontier.put((manhattan_distance(child) + cost, cost, child))
                max_pq_nodes = max(max_pq_nodes, frontier.qsize())
    
    return None, expanded_nodes, max_pq_nodes, goal_depth  


#---------------------------------------------------------------------------------------------------

def main(): # prompt

    print("--------------------------------------------------------------------------------")
    print("Welcome to 8 Tile Puzzle Solver.\n")
    # cont_program = True
    print("Type '1' to use a default puzzle, or '2' to enter your own puzzle.")
    choice = input()

    if choice == '1':
        print("Choose a default (test-case) puzzle to solve: ") # based on given pdf
        print("     1: Depth 0")
        print("     2: Depth 2")
        print("     3: Depth 4")
        print("     4: Depth 8")
        print("     5: Depth 12")
        print("     6: Depth 16")
        print("     7: Depth 20")
        print("     8: Depth 24")

        puzzle_choice = input()

        if puzzle_choice == '1':
            puzzle = test_cases["depth_0"]
        elif puzzle_choice == '2':
            puzzle = test_cases["depth_2"]
        elif puzzle_choice == '3':
            puzzle = test_cases["depth_4"]
        elif puzzle_choice == '4':
            puzzle = test_cases["depth_8"]
        elif puzzle_choice == '5':
            puzzle = test_cases["depth_12"]
        elif puzzle_choice == '6':
            puzzle = test_cases["depth_16"]
        elif puzzle_choice == '7':
            puzzle = test_cases["depth_20"]
        elif puzzle_choice == '8':
            puzzle = test_cases["depth_24"]
        else:
            print("Invalid choice. Please enter a valid option. Exiting.")
            return
    elif choice == '2':
        print("Enter your puzzle, use a ZERO to represent the blank\n")
        print("Enter the first row, use space or tabs between numbers\n")
        row1 = list(map(int, input().split()))
        print("Enter the second row, use space or tabs between numbers\n")
        row2 = list(map(int, input().split()))
        print("Enter the third row, use space or tabs between numbers\n")
        row3 = list(map(int, input().split()))
        puzzle = [row1, row2, row3]
    else:
        print("Invalid choice. Exiting.")
        return

    print("Enter your choice of algorithm\n")
    print("   1: Uniform Cost Search")
    print("   2: A* with the Misplaced Tile Heuristic")
    print("   3: A* with the Manhattan Distance Heuristic")

    algorithm = input()
    print("Algorithm chosen: " + algorithm)

    if algorithm == "1":
        print("Uniform Cost Search: ")
        sol, expanded_nodes, max_pq_nodes, goal_depth = uniform_cost_search(puzzle)
        if sol:
            print("-------GOAL---------")
            print("Search algorithm expanded a total of " + str(expanded_nodes) + " nodes.")
            print("Maximum number of nodes in the queue at any one time: " + str(max_pq_nodes) + ".")
            print("The depth of the goal node was " + str(goal_depth) + ".")
        else:
            print("Goal state not found.")
            print("Search algorithm expanded a total of " + str(expanded_nodes) + " nodes.")
            print("Maximum number of nodes in the queue was: " + str(max_pq_nodes) + ".")
    elif algorithm == "2":
        print("A* Misplaced Tile Heuristic: ")
        sol, expanded_nodes, max_pq_nodes, goal_depth = a_star_misplaced_heuristic(puzzle)
        if sol:
            print("-------GOAL---------")
            print("Search algorithm expanded a total of " + str(expanded_nodes) + " nodes.")
            print("Maximum number of nodes in the queue at any one time: " + str(max_pq_nodes) + ".")
            print("The depth of the goal node was " + str(goal_depth) + ".")
        else:
            print("Goal state not found.")
            print("Search algorithm expanded a total of " + str(expanded_nodes) + " nodes.")
            print("Maximum number of nodes in the queue was: " + str(max_pq_nodes) + ".")
    elif algorithm == "3":
        print("A* with the Manhattan Distance Heuristic: ")
        sol, expanded_nodes, max_pq_nodes, goal_depth = a_star_manhattan_heuristic(puzzle)
        if sol:
            print("-------GOAL---------")
            print("Search algorithm expanded a total of " + str(expanded_nodes) + " nodes.")
            print("Maximum number of nodes in the queue at any one time: " + str(max_pq_nodes) + ".")
            print("The depth of the goal node was " + str(goal_depth) + ".")
        else:
            print("Goal state not found.")
            print("Search algorithm expanded a total of " + str(expanded_nodes) + " nodes.")
            print("Maximum number of nodes in the queue was: " + str(max_pq_nodes) + ".")
    else:
        print("Invalid choice. Please enter a valid option. Exiting.")
        return

if __name__ == "__main__":
    main()