class SudokuSolver:

    def __init__(self, board):
        self.board = board
        self.boardLen = len(board)

    def showBoard(self):
        """
            Prints the board
        """

        for i in range(self.boardLen):
            if i % 3 == 0 and i != 0:
                print('---------------------')
            for j in range(self.boardLen):
                if j % 3 == 0 and j != 0:
                    print('| ', end='')
                if j == 8:
                    print(self.board[i][j])
                else:
                    print(f'{self.board[i][j]} ', end='')

    def isEmpty(self):
        """
            Return a tuple (row, column) with the first empty space found
        """

        for i in range(self.boardLen):
            for j in range(self.boardLen):
                if not self.board[i][j]:
                    return i, j
        return None

    def isValid(self, num, pos):
        """
            Given a number and the coordinates of an empty space in the board, 
            checks if the number is valid for this position
        """

        # Checking row validation
        for i in range(self.boardLen):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False

        # Checking column validation
        for j in range(self.boardLen):
            if self.board[j][pos[1]] == num and pos[0] != j:
                return False

        # Checking square validation
        x = pos[1] // 3
        y = pos[0] // 3

        for i in range(y * 3, y * 3 + 3):
            for j in range(x * 3, x * 3 + 3):
                if self.board[i][j] == num and (i, j) != pos:
                    return False

        return True

    def solve(self):
        """
            Main method to solve the sudoku
            It uses backtracking method to find the solution
        """

        emptyValues = self.isEmpty()
        if emptyValues is None:
            return True
        else:
            row, column = emptyValues

        for num in range(1, 10):
            if self.isValid(num, (row, column)):
                self.board[row][column] = num

                if self.solve():
                    return True

                self.board[row][column] = 0

        return False
