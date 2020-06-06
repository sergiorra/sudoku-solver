from sudoku_utils import SudokuSolver


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


print(f'###### Sudoku Solver ######')
initialBoard = getBoardInput()

if initialBoard is not None:
    sudokuSolver = SudokuSolver(initialBoard)
    sudokuSolver.showBoard()
