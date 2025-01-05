from collections import deque
class WaterJug:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
    
    def goal_test(self, current_state):
        if (current_state[0] == self.goal_state[0]):
            return True
        else:
            return False
        
    def successor(self, state):
        x, y = state
        successors = []
        capacity_x, capacity_y = 4, 3  # Capacities of the 4L and 3L jugs.
        
        # Empty the 4L jug
        successors.append((0, y))
        # Empty the 3L jug
        successors.append((x, 0))
        # Fill the 4L jug
        successors.append((capacity_x, y))
        # Fill the 3L jug
        successors.append((x, capacity_y))
        # Pour water from 4L to 3L until the 3L jug is full or the 4L jug is empty
        transfer = min(x, capacity_y - y)
        successors.append((x - transfer, y + transfer))
        # Pour water from 3L to 4L until the 4L jug is full or the 3L jug is empty
        transfer = min(y, capacity_x - x)
        successors.append((x + transfer, y - transfer))
        return successors
    
    def generate_path(self, state, parents):
        path = []
        while state is not None:
            path.append(state)
            state = parents[state]  # Trace back the parent of the current state.
        path.reverse()
        return path
    
    def bfs(self):
        open_list = deque([self.initial_state])  # Queue for BFS (FIFO)
        closed_list = set()  # Set of visited states
        parents = {self.initial_state: None}  # Track the parent of each state

        while open_list:
            current_state = open_list.popleft()  # Get the next state to explore

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


# Execute the BFS program
initial_state = (0, 0)  # 4L jug full, 3L jug empty
goal_state = (2, None)  # Goal: 2 liters in the 4L jug
bfs_solver = WaterJug(initial_state, goal_state)
bfs_solution = bfs_solver.bfs()
print("BFS Solution Path:", bfs_solution)