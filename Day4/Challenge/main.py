###Exercise
matrix = [
    "7i3",
    "Tsi",
    "h%x",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "^r!"
]

# Initializes the output string
output = ""

#  For each column of the matrix
for col in range(len(matrix[0])):
    # For each row in the matrix
    for row in range(len(matrix)):
        # Retrieves the character of the current column and row
        char = matrix[row][col]
        # If the character is alpha, append it to the output string
        if char.isalpha():
            output += char
        # If the character is not alpha and the output string is not empty, adds a space to the output string
        elif output:
            output += " "

# Displays the output string
print(output)
###end exo