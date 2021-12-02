#!/usr/bin/env python3

def get_puzzle_input():
    with open('input') as f:
        file_input = f.readlines()

    return file_input


def solve():
    input_list = get_puzzle_input()
    depth = 0
    horizontal_position = 0
    aim = 0

    for i in input_list:
        s = i.split()
        if s[0] == "down":
            aim += int(s[1])
        elif s[0] == "up":
            aim -= int(s[1])
        elif s[0] == "forward":
            horizontal_position += int(s[1])
            depth += (aim * int(s[1]))

    print("final depth is: " + str(depth))
    print("final hori pos is: " + str(horizontal_position))
    return depth * horizontal_position


print(solve())
