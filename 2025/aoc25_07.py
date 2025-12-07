# Advent of Code 2025
# Day 07
# https://adventofcode.com/2025/day/7

year = 2025
day = 7
print(f"It's day {day} for Advent of Code {year}, let's go!")

###############################################################
# Sample playground

sample_result_1 = 0
result_1 = 0
sample_result_2 = 0
result_2 = 1

# DADDLE, YOODLE, YAY

sample_input = '''\
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''

with open('aoc25_07_input.txt') as f:
    for line in f:
        first_line = line.rstrip('\n')
        break

#first_line = lines[0]
l = len(first_line)
tachyon_line = l*['.']
for i, c in enumerate(first_line):
    if c == 'S':
        tachyon_line[i] = '|'
#print(tachyon_line)

def tachyonize(input_line, prev_tachyon_line):
    splits = 0
    line_as_list = [c for c in input_line]
    for i, c in enumerate(line_as_list):
        if prev_tachyon_line[i] == '|':
            if line_as_list[i] == '.':
                line_as_list[i] = '|'
            elif line_as_list[i] == '^':
                splits += 1
                line_as_list[i-1] = '|'
                line_as_list[i+1] = '|'
    return splits, line_as_list

def tachyonize_num(input_line, prev_num_tachyon_line):
    splits = 0
    line_as_list = [c for c in input_line]
    output_line = l*[0]
    for i, c in enumerate(line_as_list):
        if prev_num_tachyon_line[i] >= 1:
            if line_as_list[i] == '.':
                output_line[i] += prev_num_tachyon_line[i]
            elif line_as_list[i] == '^':
                splits += 1
                output_line[i-1] += prev_num_tachyon_line[i]
                output_line[i+1] += prev_num_tachyon_line[i]
    return splits, output_line


with open('aoc25_07_input.txt') as f:
    f.readline()

    prev_line = tachyon_line
    for input_line in f:
        input_line = input_line.rstrip()
        splits, prev_line = tachyonize(input_line, prev_line)
        result_1 += splits

#print(f"The result on the sample input is {sample_result_1}.")
#print(sample_result_2)
#quit()

###############################################################
# First part: count splits encountered

print(f"The first result is {result_1}.")
#quit()

###############################################################
# Second part: count paths

#lines = sample_input.split('\n')
#first_line = lines[0].rstrip()
#l = len(first_line)
num_tachyon_line = l*[0]
for i, c in enumerate(first_line):
    if c == 'S':
        num_tachyon_line[i] = 1
#print(num_tachyon_line)
#print(tachyon_line)
num_line = num_tachyon_line 

#for line in lines[1:]:
with open('aoc25_07_input.txt') as f:
    f.readline()

    num_line = num_tachyon_line
    for line in f:
        line = line.rstrip()
        _, num_line = tachyonize_num(line, num_line)
    #print(num_line)

result_2 = sum(num_line)

#print(f"The result for part 2 on the sample input is {sample_result_2}.")
print(f"The second result is {result_2}.")
