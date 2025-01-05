# Function to check if a line (row, column, or diagonal) is open for a player
def is_open_for_player(line, player):
    return all(cell == player or cell == ' ' for cell in line)

# Function to check if a line (row, column, or diagonal) is open for the opponent
def is_open_for_opponent(line, opponent):
    return all(cell == opponent or cell == ' ' for cell in line)

# Function to calculate the heuristic value of the Tic-Tac-Toe state
def calculate_heuristic(board, player, opponent):
    heuristic = 0
    
    # Check rows and columns
    for i in range(3):
        row = board[i]
        column = [board[j][i] for j in range(3)]
        
        # Check if the row is open for the player or opponent
        if is_open_for_player(row, player):
            heuristic += 1
        if is_open_for_opponent(row, opponent):
            heuristic -= 1
            
        # Check if the column is open for the player or opponent
        if is_open_for_player(column, player):
            heuristic += 1
        if is_open_for_opponent(column, opponent):
            heuristic -= 1
    
    # Check diagonals
    diagonal1 = [board[i][i] for i in range(3)]
    diagonal2 = [board[i][2-i] for i in range(3)]
    
    # Check if the diagonal is open for the player or opponent
    if is_open_for_player(diagonal1, player):
        heuristic += 1
    if is_open_for_opponent(diagonal1, opponent):
        heuristic -= 1
    if is_open_for_player(diagonal2, player):
        heuristic += 1
    if is_open_for_opponent(diagonal2, opponent):
        heuristic -= 1
    
    return heuristic

# Example usage
def main():
    # Tic-Tac-Toe board (3x3 matrix)
    board = [
        ['X', ' ', 'O'],
        [' ', 'X', ' '],
        ['O', ' ', 'X']
    ]
    
    player = 'X'
    opponent = 'O'
    
    # Calculate heuristic value for the given board
    heuristic_value = calculate_heuristic(board, player, opponent)
    
    print(f"Heuristic value for player {player} against opponent {opponent}: {heuristic_value}")

if __name__ == "__main__":
    main()
