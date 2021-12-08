#!/usr/bin/env python3

import numpy


def get_drawing_numbers():
    with open('input') as f:
        file_input = f.readlines()

    drawing_numbers = list(map(int, file_input[0].split(',')))  # convert string -> list of ints
    return drawing_numbers


# returns a list of two dimensional arrays [][] (boards)
def get_boards():
    boards = []

    # determine amount of boards
    with open('input') as newline_read:
        file_input = newline_read.readlines()

    num_boards = file_input.count('\n')

    f = open("input", "r")
    next(f)  # skip first line of file

    rows = f.read().splitlines()

    # remove all space characters from file
    while '' in rows:
        rows.remove('')

    row_position = 0

    for i in range(num_boards):
        num_rows, num_cols = (5, 5)
        board = [[0 for i in range(num_cols)] for j in range(num_rows)]  # initialize empty board

        row_ints = list(map(int, rows[row_position].split()))  # convert row to list of ints

        # populate board
        for x in range(5):
            for y in range(num_cols):
                board[x][y] = row_ints[y]

            row_position += 1
            if row_position != 500:
                row_ints = list(map(int, rows[row_position].split()))

        # add board to list of boards
        boards.append(board)

    return boards


def check_winner_row(board):
    for row in board:
        if row[0] == 0 and row[1] == 0 and row[2] == 0 and row[3] == 0 and row[4] == 0:
            print("This board wins via row!")
            for r in board:
                print(r)
            return True

    return False


def check_winner_col(board):

    array = numpy.asarray(board)

    for column in array.T:
        if column[0] == 0 and column[1] == 0 and column[2] == 0 and column[3] == 0 and column[4] == 0:
            print("This board wins via column!")
            print(array)
            return True

    return False


def calc_unmarked_sum(board):
    unmarked_sum = 0

    for row in board:
        for i in row:
            if i != 0:
                unmarked_sum += i

    return unmarked_sum


def solve():
    score = 0
    drawing_numbers = get_drawing_numbers()
    boards = get_boards()

    for num in drawing_numbers:
        for board in boards:
            for row in board:
                for i, val in enumerate(row):
                    if row[i] == num:
                        # mark that number by zeroing out that value
                        row[i] = 0

                        # call check_winner_row() to determine if this row wins horizontally
                        if check_winner_row(board):
                            print("Winning number: " + str(num))
                            unmarked_sum = calc_unmarked_sum(board)
                            score = unmarked_sum * num
                            return score

                        # call check_winner_col() to determine if this row wins vertically
                        if check_winner_col(board):
                            unmarked_sum = calc_unmarked_sum(board)
                            score = unmarked_sum * num
                            return score

    return score


def solve_last_board():
    score = 0
    drawing_numbers = get_drawing_numbers()
    boards = get_boards()

    boards_copy = boards

    for num in drawing_numbers:
        print("checking number " + str(num))
        for board in boards_copy:
            for row in board:
                for i, val in enumerate(row):
                    #print("comparing board number " + str(row[i]) + " to " + str(num))
                    if row[i] == num:
                        # mark that number by zeroing out that value
                        #print("Match! of board number " + str(row[i]) + " to " + str(num))
                        row[i] = 0

                        # issue is: after a winner is determined, the rest of the boards don't get the row[i] = 0
                        # after a winning board is seen, it just checks the rest of THAT board, and moves to next num
                        # it needs to check the other boards as well

                        # call check_winner_col() to determine if this row wins vertically
                        if check_winner_col(board):
                            print("Winning number: " + str(num))
                            if len(boards) == 1:
                                print("on last board, col")
                                unmarked_sum = calc_unmarked_sum(board)
                                score = unmarked_sum * num
                                return score
                            boards.remove(board)

                        # call check_winner_row() to determine if this row wins horizontally
                        if check_winner_row(board):
                            print("Winning number: " + str(num))
                            if len(boards) == 1:
                                print("on last board, row")
                                print(board)
                                unmarked_sum = calc_unmarked_sum(board)
                                score = unmarked_sum * num
                                return score
                            boards.remove(board)


    print(boards)
    return score


print(solve_last_board())
#print(solve())
