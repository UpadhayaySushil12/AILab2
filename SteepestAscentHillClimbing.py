import copy

class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def heuristic_misplaced_tiles(self, state):
        return sum(1 for i in range(9) if state[i] != 0 and state[i] != self.goal_state[i])

    def heuristic_manhattan_distance(self, state):
        distance = 0
        for i in range(9):
            if state[i] != 0:
                goal_index = self.goal_state.index(state[i])
                current_row, current_col = divmod(i, 3)
                goal_row, goal_col = divmod(goal_index, 3)
                distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        return distance

    def get_possible_moves(self, state):
        blank_index = state.index(0)  # Find the blank tile (0)
        row, col = divmod(blank_index, 3)

        moves = []
        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                # Swap the blank tile with the target tile
                new_index = new_row * 3 + new_col
                new_state = state[:]
                new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
                moves.append(new_state)

        return moves

    def steepest_ascent_hill_climbing(self, heuristic_function):
        current_state = self.initial_state[:]
        current_heuristic = heuristic_function(current_state)

        while current_heuristic > 0:
            print(f"Current State: {current_state}, Heuristic: {current_heuristic}")

            # Generate all possible moves
            moves = self.get_possible_moves(current_state)

            # Evaluate heuristics for each move
            successors = [(move, heuristic_function(move)) for move in moves]
            successors.sort(key=lambda x: x[1])  # Sort by heuristic value

            # Select the best move (lowest heuristic)
            best_move, best_heuristic = successors[0]

            if best_heuristic >= current_heuristic:
                # No improvement possible
                print("No better moves found. Stopping.")
                break

            # Move to the best successor
            current_state = best_move
            current_heuristic = best_heuristic

        if current_heuristic == 0:
            print("Goal state reached!")
        else:
            print("Stuck at local maximum.")

        return current_state

# Example usage
initial_state = [1, 2, 3, 0, 4, 6, 7, 5, 8]  # Example initial state
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]     # Goal state

puzzle = Puzzle(initial_state, goal_state)
final_state = puzzle.steepest_ascent_hill_climbing(puzzle.heuristic_manhattan_distance)
print(f"Final State: {final_state}")
