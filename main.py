from sudoku_solver import SudokuSolver


def getBoardInput():
    board = []
    for i in range(1, 10):
        rowValues = input(f'Enter entries for row number {i}: ')
        try:
            int(rowValues)
        except:
            print('Values not valid')
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
