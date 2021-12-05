#!/usr/bin/env python3


def get_puzzle_input():
    with open('input') as f:
        file_input = f.readlines()

    return file_input


def solve():
    input_list = get_puzzle_input()
    gamma_rate_bin = []
    epsilon_rate_bin = []

    for x in range(12):
        num_zero = 0
        num_one = 0
        for i in range(len(input_list)):
            octet = list(input_list[i].rstrip())  # convert to individual bit list

            if int(octet[x]) == 0:
                num_zero += 1
            elif int(octet[x]) == 1:
                num_one += 1

        if num_zero < num_one:
            gamma_rate_bin.append(0)
            epsilon_rate_bin.append(1)
        else:
            gamma_rate_bin.append(1)
            epsilon_rate_bin.append(0)

    gamma_rate = ''.join(map(str, gamma_rate_bin))
    epsilon_rate = ''.join(map(str, epsilon_rate_bin))

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


print(solve())
