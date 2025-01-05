import random
class ModelBasedRoomCleanerAgent:
    def __init__(self, room_size=(10, 10)):
        self.room_size = room_size
        self.grid = [[random.choice([0, 1]) for _ in range(room_size[1])] for _ in range(room_size[0])]
        self.current_position = (random.randint(0, room_size[0] - 1), random.randint(0, room_size[1] - 1))
        self.cleaned_cells = set()  # Track cleaned cells

    def display_room(self):
        for row in self.grid:
            print(' '.join(str(cell) for cell in row))
        print()

    def perceive(self):
        x, y = self.current_position
        return self.grid[x][y]

    def act(self):
        x, y = self.current_position
        if self.perceive() == 1:  # Dirty cell
            print(f"Cell ({x}, {y}) is Dirty. Cleaning...")
            self.grid[x][y] = 0  # Clean cell
            self.cleaned_cells.add((x, y))  # Update model
            print(f"Cell ({x}, {y}) is now Clean.")
        else:
            print(f"Cell ({x}, {y}) is already Clean.")

    def find_nearest_dirty_cell(self):
        # Find the nearest dirty cell based on Manhattan distance
        dirty_cells = [
            (i, j) for i in range(self.room_size[0]) 
            for j in range(self.room_size[1]) 
            if self.grid[i][j] == 1
        ]
        if not dirty_cells:
            return None  # All cells are clean
        x, y = self.current_position
        return min(dirty_cells, key=lambda cell: abs(cell[0] - x) + abs(cell[1] - y))

    def move(self):
        next_cell = self.find_nearest_dirty_cell()
        if next_cell:
            self.current_position = next_cell
        else:
            self.current_position = None  # No more dirty cells

    def is_room_clean(self):
        return all(cell == 0 for row in self.grid for cell in row)

    def run(self):
        print("Initial Room Status:")
        self.display_room()

        steps = 0
        while not self.is_room_clean():
            print(f"\nStep {steps + 1}:")
            self.act()
            self.move()
            steps += 1
            if self.current_position is None:
                break

        print("\nFinal Room Status:")
        self.display_room()
        print(f"Room cleaned in {steps} steps.")

# Create and run the Model-Based Room Cleaner Agent
agent = ModelBasedRoomCleanerAgent()
agent.run()
