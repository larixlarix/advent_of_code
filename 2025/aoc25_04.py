# Advent of Code 2025
# Day 04
# https://adventofcode.com/2025/day/4

year = 2025
day = 4
print(f"It's day {day} for Advent of Code {year}, let's go!")

###############################################################
# Sample playground

sample_result_1 = 0
result_1 = 0
sample_result_2 = 0
result_2 = 0

# DADDLE, YOODLE, YAY

sample_input = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''


def to_num(char):
    return 1 if char=='@' else 0

def neighbors(grid, i, j):
    # number of 1s in the eight adjacent fields at pos i, j in the numerical grid
    n = 0
    for u, v in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
        n += grid[i+u][j+v]
    return n

#print(sample_result_1)
#print(sample_result_2)
#quit()

###############################################################
# First part

with open('aoc25_04_input.txt') as f:
    w = len(f.readline().strip('\n'))

# generate padded numerical grid

top_bottom_line = [0 for _ in range(w+2)]
padded_grid = [top_bottom_line]

h = 0

with open('aoc25_04_input.txt') as f:
    for line in f:
        line = line.strip('\n')
        h +=1
        padded_line = [0]
        padded_line.extend([to_num(c) for c in line])
        padded_line.append(0)
        padded_grid.append(padded_line)

padded_grid.append(top_bottom_line)
# print(h, w)

# evaluate padded grid
# print(padded_grid)

for i in range(1, h+1):
    for j in range (1, w+1):
        if padded_grid[i][j] == 1 and neighbors(padded_grid, i, j) < 4:
            #print(i, j)
            result_1 +=1
        
print(f"The first result is {result_1}.")
#quit()

###############################################################
# Second part: Remove removable rolls

result_2 = 0
try_more = True
while try_more:
    try_more = False
    for i in range(1, h+1):
        for j in range (1, w+1):
            if padded_grid[i][j] == 1 and neighbors(padded_grid, i, j) < 4:
                padded_grid[i][j] = 0
                result_2 +=1
                try_more = True
        

print(f"The second result is {result_2}.")