class WaterJugDFS:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def goal_test(self, current_state):
        return current_state[0] == self.goal_state[0]

    def successor(self, state):
        x, y = state
        successors = []
        capacity_x, capacity_y = 4, 3
        successors.append((0, y))
        successors.append((x, 0))
        successors.append((capacity_x, y))
        successors.append((x, capacity_y))
        transfer = min(x, capacity_y - y)
        successors.append((x - transfer, y + transfer))
        transfer = min(y, capacity_x - x)
        successors.append((x + transfer, y - transfer))

        return successors

    def generate_path(self, state, parents):
        path = []
        while state is not None:
            path.append(state)
            state = parents[state]
        path.reverse()
        return path

    def dfs(self):
        open_list = [self.initial_state]  # Stack for DFS (LIFO)
        closed_list = set()  # Set of visited states
        parents = {self.initial_state: None}  # Track the parent of each state

        while open_list:
            current_state = open_list.pop()  # Get the next state to explore

            # Check if the goal state is reached
            if self.goal_test(current_state):
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


initial_state = (0, 0) 
goal_state = (2, None) 
dfs_solver = WaterJugDFS(initial_state, goal_state)
dfs_solution = dfs_solver.dfs()
print("DFS Solution Path:", dfs_solution)
