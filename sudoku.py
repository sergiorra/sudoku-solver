from sudoku_utils import SudokuSolver


def getBoardInput():
    board = []
    for i in range(1, 10):
        row_values = input(f'Enter entries of row number {i}: ')
        try:
            int(row_values)
        except:
            print('Values not valid')
            return None
        board.append([int(i) for i in str(row_values)])
    return board


initial_board = getBoardInput()

if initial_board is not None:
    sudoku_solver = SudokuSolver(initial_board)
    print(sudoku_solver.board)
