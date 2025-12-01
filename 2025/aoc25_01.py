# Advent of Code 2025
# Day 01
# https://adventofcode.com/2025/day/1

n_dial_points_to = 50
n_zeros = 0

with open('aoc25_01_input.txt') as f:
    for line in f:
        if line[0] == "L":
            n_dial_points_to -= int(line[1:])
        elif line[0] == "R":
            n_dial_points_to += int(line[1:])
        else:
            continue
        n_dial_points_to = n_dial_points_to % 100

        if n_dial_points_to == 0:
            n_zeros +=1

print(f"The actual code is: {n_zeros}.")


n_dial_points_to = 50
n_zeros_passed = 0

with open('aoc25_01_input.txt') as f:
    for line in f:
        steps = int(line[1:])
        for i in range(steps):
            if line[0] == "L":
                n_dial_points_to -=1
            elif line[0] == "R":
                n_dial_points_to += 1
            else:
                continue
            n_dial_points_to = n_dial_points_to % 100

            if n_dial_points_to == 0:
                n_zeros_passed +=1

print(f"The actual code using method 0x434C49434B is: {n_zeros_passed}.")