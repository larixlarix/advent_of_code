# Advent of Code 2025
# Day 05
# https://adventofcode.com/2025/day/5

year = 2025
day = 5
print(f"It's day {day} for Advent of Code {year}, let's go!")

###############################################################
# Sample playground

sample_result_1 = 0
result_1 = 0
sample_result_2 = 0
result_2 = 0

# DADDLE, YOODLE, YAY

sample_input = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''


def process_input(input):
    fresh_ranges = []
    ingredients = []
    process_upper_input = True

    for line in input.split('\n'):
        if process_upper_input:
            if len(line)==0:
                process_upper_input = False
                continue
            else:    
                fresh_range = [int(i) for i in line.strip().split('-')]
                fresh_ranges.append(fresh_range)
        else:
            ingredients.append(int(line))

    return fresh_ranges, ingredients

#print(sample_result_1)
#print(sample_result_2)
#quit()

###############################################################
# First part

with open('aoc25_05_input.txt') as f:
    fresh_ranges, ingredients  = process_input(f.read())

fresh_ingredients = []
for ingredient in ingredients:
    is_fresh = False

    for fresh_range in fresh_ranges:
        a, b = fresh_range
        if a <= ingredient <= b+1:
            is_fresh = True
            fresh_ingredients.append(ingredient)
            break

result_1 = len(set(fresh_ingredients))
print(f"The first result is {result_1}.")
#quit()

###############################################################
# Second part: Fresh ingredient IDs
result_2 = 0

#fresh_ranges, _ = process_input(sample_input)
list_of_as = []
list_of_bs = []

for i, fresh_range in enumerate(fresh_ranges):
    a, b = fresh_range
    list_of_as.append(a)
    list_of_bs.append(b)

sorted_as = sorted(list_of_as)
sorted_bs = sorted(list_of_bs)

a_min = sorted_as[0]
b_max = sorted_bs[-1]
 
result_2 = b_max+1-a_min
# correct for IDs that not in any fresh_range intervals
for i, a in enumerate(sorted_as):
    list_smaller_b = [b for b in list_of_bs if b+1 < a]
    if len(list_smaller_b) >= i >= 1:
        result_2 -= (a - sorted_bs[i-1] - 1)

print(f"The second result is {result_2}.")
