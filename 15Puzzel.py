import random

class Tile:
    def __init__(self, value, position):
        self.value = value
        self.position = position

class Puzzle:
    def __init__(self):
        self.tiles = []
        for i in range(16):
            self.tiles.append(Tile(i, i))

    def shuffle(self):
        random.shuffle(self.tiles)

    def is_solvable(self):
        # Check if the parity of the permutation of the tiles is even
        parity = 0
        for i in range(15):
            for j in range(i + 1, 16):
                if self.tiles[i].value > self.tiles[j].value:
                    parity += 1
        # Check if the parity of the taxicab distance between the empty tile and the bottom right corner is even
        empty_tile_position = self.tiles[15].position
        taxicab_distance = abs(empty_tile_position % 4 - 3) + abs(empty_tile_position // 4 - 3)
        return parity % 2 == taxicab_distance % 2

    def solve(self):
        # Use the A* algorithm to find the shortest path to the goal state
        queue = []
        queue.append((self, 0))
        visited = set()
        while queue:
            state, cost = queue.pop(0)
            if state.is_goal():
                return cost
            for neighbor in state.get_neighbors():
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, cost + 1))
        return -1

    def get_neighbors(self):
        neighbors = []
        empty_tile_position = self.tiles[15].position
        # Move the empty tile up
        if empty_tile_position >= 4:
            neighbor = Puzzle()
            neighbor.tiles = self.tiles[:]
            neighbor.tiles[empty_tile_position], neighbor.tiles[empty_tile_position - 4] = neighbor.tiles[empty_tile_position - 4], neighbor.tiles[empty_tile_position]
            neighbors.append(neighbor)
        # Move the empty tile down
        if empty_tile_position < 12:
            neighbor = Puzzle()
            neighbor.tiles = self.tiles[:]
            neighbor.tiles[empty_tile_position], neighbor.tiles[empty_tile_position + 4] = neighbor.tiles[empty_tile_position + 4], neighbor.tiles[empty_tile_position]
            neighbors.append(neighbor)
        # Move the empty tile left
        if empty_tile_position % 4 != 0:
            neighbor = Puzzle()
            neighbor.tiles = self.tiles[:]
            neighbor.tiles[empty_tile_position], neighbor.tiles[empty_tile_position - 1] = neighbor.tiles[empty_tile_position - 1], neighbor.tiles[empty_tile_position]
            neighbors.append(neighbor)
        # Move the empty tile right
        if empty_tile_position % 4 != 3:
            neighbor = Puzzle()
            neighbor.tiles = self.tiles[:]
            neighbor.tiles[empty_tile_position], neighbor.tiles[empty_tile_position + 1] = neighbor.tiles[empty_tile_position + 1], neighbor.tiles[empty_tile_position]
            neighbors.append(neighbor)
        return neighbors

    def is_goal(self):
        for i in range(15):
            if self.tiles[i].value != i:
                return False
        return True

    def print(self):
        for i in range(4):
            for j in range(4):
                print(self.tiles[i * 4 + j].value, end=" ")
            print()

def main():
    puzzle = Puzzle()
    puzzle.shuffle()
    if puzzle.is_solvable():
        print("The puzzle is solvable.")
        cost = puzzle.solve()
        print("The shortest path to the goal state has", cost, "moves.")
    else:
        print("The puzzle is not solvable.")

if __name__ == "__main__":
    main()