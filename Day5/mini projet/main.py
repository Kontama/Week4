grid = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# list of players
players = ['O', 'X']

# Clue of the current player in the list of players
current_player_index = 0

# Function to display the grid
def print_grid():
    for row in grid:
        print(' '.join(row))

# Function to check if a player has won
def check_win(player):
    # Checks rows
    for row in grid:
        if row == [player, player, player]:
            return True
    # Checks columns
    for col in range(3):
        if grid[0][col] == player and grid[1][col] == player and grid[2][col] == player:
            return True
    # Checks diagonals
    if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
        return True
    if grid[0][2] == player and grid[1][1] == player and grid[2][0] == player:
        return True
    # No player won
    return False

# Game loop
while True:
    # Displays the grid
    print_grid()
    # Prompts the user to enter a row and column
    row = int(input("Saisissez une ligne (0, 1 ou 2) : "))
    col = int(input("Saisissez une colonne (0, 1 ou 2) : "))
    # Verifies that the box entered is empty
    if grid[row][col] == ' ':
        # Place the current player's mark in the box
        grid[row][col] = players[current_player_index]
        #  Checks if the current player has won
        if check_win(players[current_player_index]):
            print("Le joueur " + players[current_player_index] + " a gagné !")
            break
        # Move on to next player
        current_player_index = (current_player_index + 1) % 2
    else:
        print("Case déjà occupée, veuillez en choisir une autre.")
    # Checks if the grid is full
    if all(all(cell != ' ' for cell in row) for row in grid):
        print("Match nul !")
        break