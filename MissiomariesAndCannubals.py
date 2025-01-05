from collections import deque

class MissionariesAndCannibals:
    def __init__(self):
        self.initial_state = (3, 3, 1)  # (Missionaries on left, Cannibals on left, Boat position: 1=left, 0=right)
        self.goal_state = (0, 0, 0)    # (All moved to the right side)

    def is_valid_state(self, state):
        m_left, c_left, _ = state # _  is called place holder
        m_right, c_right = 3 - m_left, 3 - c_left

        # Check if numbers are within valid bounds
        if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
            return False

        # Check constraints: Missionaries >= Cannibals on both sides (if missionaries > 0)
        if (m_left > 0 and m_left < c_left) or (m_right > 0 and m_right < c_right):
            return False

        return True

    def successor(self, state):
        m_left, c_left, boat_pos = state
        successors = []
        boat_moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]  # Possible moves: (M, C)

        for m, c in boat_moves:
            if boat_pos == 1:  # Boat on the left side
                new_state = (m_left - m, c_left - c, 0)
            else:  # Boat on the right side
                new_state = (m_left + m, c_left + c, 1)

            if self.is_valid_state(new_state):
                successors.append(new_state)

        return successors

    def generate_path(self, state, parents):
        path = []
        while state is not None:
            path.append(state)
            state = parents[state]
        path.reverse()
        return path

    def bfs(self):
        open_list = deque([self.initial_state])  # Queue for BFS (FIFO)
        closed_list = set()  # Set of visited states
        parents = {self.initial_state: None}  # Track the parent of each state

        while open_list:
            current_state = open_list.popleft()  # Get the next state to explore

            # Check if the goal state is reached
            if current_state == self.goal_state:
                return self.generate_path(current_state, parents)

            # Mark the current state as visited
            if current_state in closed_list:
                continue
            closed_list.add(current_state)

            # Generate and process successors
            for successor in self.successor(current_state):
                if successor not in closed_list and successor not in open_list:
                    open_list.append(successor)
                    parents[successor] = current_state  # Record the parent of the successor

        return None  # No solution found


# Execute the BFS program
solver = MissionariesAndCannibals()
solution = solver.bfs()
if solution:
    print("Solution Path:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
