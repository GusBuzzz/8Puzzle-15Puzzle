import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = 0 if parent is None else parent.cost + 1

    def __lt__(self, other):
        return (self.cost + self.heuristic()) < (other.cost + other.heuristic())

    def __eq__(self, other):
        return isinstance(other, PuzzleNode) and self.state == other.state

    def __hash__(self):
        return hash(tuple(self.state))

    def get_blank_position(self):
        row = self.state.index(0) // 3
        col = self.state.index(0) % 3
        return row, col

    def get_neighbors(self):
        row, col = self.get_blank_position()
        neighbors = []

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = list(self.state)
                new_state[row * 3 + col], new_state[new_row * 3 + new_col] = new_state[new_row * 3 + new_col], new_state[row * 3 + col]
                neighbors.append(PuzzleNode(new_state, self, (dr, dc)))

        return neighbors

    def is_goal(self, goal_state):
        return self.state == goal_state

    def heuristic(self):
        # Manhattan distance heuristic
        distance = 0
        for i in range(1, 9):
            current_position = self.state.index(i)
            goal_position = goal_state.index(i)
            distance += abs(current_position // 3 - goal_position // 3) + abs(current_position % 3 - goal_position % 3)
        return distance

def solve_8_puzzle(initial_state, goal_state):
    start_node = PuzzleNode(initial_state)
    goal_node = PuzzleNode(goal_state)

    open_set = [start_node]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.is_goal(goal_state):
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node)

        for neighbor in current_node.get_neighbors():
            if neighbor not in closed_set and neighbor not in open_set:
                heapq.heappush(open_set, neighbor)

    return None

if __name__ == '__main__':
    initial_state = [1, 8, 3, 4, 0, 7, 6, 5, 2]
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    solution_path = solve_8_puzzle(initial_state, goal_state)
    if solution_path:
        for step, state in enumerate(solution_path):
            print(f"Step {step + 1}: {state}")
    else:
        print("No solution found.")
