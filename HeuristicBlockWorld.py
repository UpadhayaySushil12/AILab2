class BlocksWorld:
    def __init__(self, initial_state, goal_state):
        """
        Initialize the BlocksWorld problem with initial and goal states.
        Each state is represented as a list of stacks.
        """
        self.initial_state = initial_state
        self.goal_state = goal_state

    def calculate_heuristic(self, state):
        """
        Calculate the heuristic value of a given state.
        Heuristic rules:
        - +1 for each block in a correct support structure.
        - -1 for each block in an incorrect support structure.
        """
        heuristic_value = 0
        for stack_index, stack in enumerate(state):
            for block_index, block in enumerate(stack):
                # Check if the current block is in the goal state
                if stack_index < len(self.goal_state) and block_index < len(self.goal_state[stack_index]):
                    # Compare block's position in current state and goal state
                    if block == self.goal_state[stack_index][block_index]:
                        heuristic_value += (block_index + 1)  # Add +1 for the block and all blocks below it
                    else:
                        heuristic_value -= (block_index + 1)  # Subtract -1 for the block and all blocks below it
                else:
                    heuristic_value -= (block_index + 1)  # Subtract -1 for incorrect blocks
        return heuristic_value


# Example: Define the initial and goal states
initial_state = [
    ['A', 'D'],  # Stack 1
    ['C', 'B'],  # Stack 2
]

goal_state = [
    ['C'],       # Stack 1
    ['B'],       # Stack 2
    ['A', 'D'],  # Stack 3
]

# Create an instance of BlocksWorld
blocks_world = BlocksWorld(initial_state, goal_state)

# Calculate heuristic value for the initial state
heuristic_value = blocks_world.calculate_heuristic(initial_state)
print(f"Heuristic value for the given state: {heuristic_value}")
