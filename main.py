import argparse
from src import sudoku

def main(input_file:str):

    game = sudoku(input_file)
    game.hill_Climbing()
    game.show_board()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                prog = 'Sudoku',
                description = 'use hill climbing to solve sudoku',
                epilog = 'Text at the bottom of help')

    parser.add_argument('--input_file', type=str)
    args = parser.parse_args()
    main(args.input_file)