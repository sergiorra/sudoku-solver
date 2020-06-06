class SudokuSolver:

    def __init__(self, board):
        self.board = board

    def showBoard(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print('---------------------')
            for j in range(len(self.board)):
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
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if not self.board[i][j]:
                    return i, j
        return None
