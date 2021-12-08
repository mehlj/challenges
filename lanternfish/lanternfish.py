#!/usr/bin/env python3

def get_puzzle_input():
    with open('input') as f:
        file_input = f.read()

    file_input = (file_input.rstrip()).split(",")  # split by commas and remove newline

    # convert strings in list to int
    for i in range(len(file_input)):
        file_input[i] = int(file_input[i])

    return file_input


def solve():
    state = get_puzzle_input()

    days = 80

    while days != 0:
        for index, value in enumerate(state):
            if value != 0:
                state[index] = value - 1

            if value == 0:
                state[index] = 6
                state.append(9)

        days -= 1

    return str(len(state))


print(solve())
