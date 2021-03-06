from sudoku_solver import SudokuSolver


def getBoardInput():
    board = []
    for i in range(1, 10):
        rowValues = input(f'Enter entries for row number {i}: ')
        try:
            int(rowValues)
        except ValueError:
            print('Input values not valid')
            return None
        if len(str(rowValues)) != 9:
            print('You need to enter 9 values for each row')
            return None
        rowList = [int(i) for i in str(rowValues)]
        board.append(rowList)
    return board


print(f'############## Sudoku Solver ##############')
print(f'Program that solves a 9x9 Sudoku, let\'s go!\n')

initialBoard = getBoardInput()

if initialBoard is not None:
    sudokuSolver = SudokuSolver(initialBoard)
    if sudokuSolver.solve():
        print('#####################')
        sudokuSolver.showBoard()
        print('#####################')
    else:
        print('The sudoku could not be solved')
