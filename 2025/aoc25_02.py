# Advent of Code 2025
# Day 02
# https://adventofcode.com/2025/day/2

result_1 = 0

sample_line = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124'''

with open('aoc25_02_input.txt') as f:
    for line in f:
        for interval in line.split(','):
            a, b = interval.split('-')
            for i in range(int(a), int(b)+1):
                l = len(str(i))
                if l%2 == 0:
                    if str(i)[:int(l/2)] == str(i)[int(l/2):]:
                        result_1 += i
                else:
                    continue

print(f"The result is {result_1}.")


###############################################################
# Second part: add numbers made only of some sequence of digits 
# repeated at least twice

result_2 = 0

import re
pattern = re.compile(r"^(\d+)(\1)+$")

with open('aoc25_02_input.txt') as f:
    for line in f:
        for interval in line.split(','):
            a, b = interval.split('-')
            for i in range(int(a), int(b)+1):
                if pattern.match(str(i)) is not None:
                    result_2 += i

print(f"The second result is: {result_2}.")