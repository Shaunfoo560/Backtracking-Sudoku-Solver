# Random example board
board = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]]

# Function to check for filled squares
def valid(board, row, col, number):
        for i in range(len(board)):
                if board[row][i] == number:
                        return False

        for i in range(len(board)):
                if board[i][col] == number:
                        return False

        for i in range(len(board) // 3):
                for j in range(len(board) // 3):
                        if board[row - row % 3 + i][col - col % 3 + j] == number:
                                return False

        return True

# Recursive solving function
def solve(board, row, col):
        # Base case
        if col == 9:
                if row == 8:
                        return True
                row += 1
                col = 0

        # If square has already been filled in, call solve on next
        if board[row][col] != 0:
                return solve(board, row, col + 1)

        # Testing which value to fill in
        for i in range(1, 10):
                if valid(board, row, col, i):
                        board[row][col] = i
                        if solve(board, row, col + 1):
                                return True
                board[row][col] = 0
        return False

# Printing the board
if solve(board, 0, 0):
        for i in range(9):
                if i % 3 == 0 and i != 0:
                        print("------+-------+-------")

                for j in range(9):
                        if j % 3 == 0 and j != 0:
                                print("| ", end="")

                        if j == 8:
                                print(board[i][j])

                        else:
                                print(str(board[i][j]) + " ", end="")

else:
        print("Unsolvable")
