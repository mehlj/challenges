

""" Authentication is required for grabbing puzzle input
#import requests
#def get_http_puzzle_input():
#	url = "https://adventofcode.com/2021/day/1/input"
#	file = requests.get(url)
#	print(file.text)
"""


def get_puzzle_input():
    with open('input') as f:
        file_input = f.readlines()
        file_input = [int(i) for i in file_input]

    return file_input


def solve():
    input_list = get_puzzle_input()
    num_increases = 0

    for i in range(len(input_list)):
        if (input_list[i] > input_list[i-1]) and (i != 0):
            print("Increase at index: " + str(i) + ", from " + str(input_list[i-1]) + " to " + str(input_list[i]))
            num_increases += 1

    return num_increases


print(solve())
