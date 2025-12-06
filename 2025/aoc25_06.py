# Advent of Code 2025
# Day 06
# https://adventofcode.com/2025/day/6

year = 2025
day = 6
print(f"It's day {day} for Advent of Code {year}, let's go!")

###############################################################
# Sample playground

sample_result_1 = 0
result_1 = 0
sample_result_2 = 0
result_2 = 0

# DADDLE, YOODLE, YAY

sample_input = '''\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  \
'''

def process_input(input):
    data = [line.rstrip('\n') for line in input.split('\n')]
    operator_list = list(data[-1].split())
    return data, operator_list

def math_homework(input):
    data, operator_list = process_input(input)
    
    column_results = list(map(lambda op: 1 if op == '*' else 0, operator_list))

    for line in data[:-1]:
        for i, n in enumerate(line.split()):
            if operator_list[i] == '*':
                column_results[i] *= int(n)
            else:
                column_results[i] += int(n)
    return sum(column_results)

sample_result_1 = math_homework(sample_input)
print(f"The result on the sample input is {sample_result_1}.")
#print(sample_result_2)
#quit()

###############################################################
# First part

with open('aoc25_06_input.txt') as f:
    result_1 = math_homework(f.read())

print(f"The first result is {result_1}.")
#quit()

###############################################################
# Second part: read cephalopod math the right way

def cephalopod_math_homework(input):
    data, operator_list = process_input(input)
    l = len(data)

    exercise_positions = []
    for i, c in enumerate(data[-1]):
        if c in ['*', '+']:
            exercise_positions.append(i)
    exercise_positions.append(len(data[0])+1)
    
    total = 0
    for i, op in enumerate(operator_list):
        numbers = []
        stop_col, start_col = exercise_positions[i]-1, exercise_positions[i+1]-2
        for j in range(start_col, stop_col, -1):
            n = str()
            for k in range(l-1):
                n += (data[k][j])
            numbers.append(int(n))
        #print(numbers)
        if op == '+':
            result = sum(numbers)
        else:
            result = 1
            for n in numbers:
                result *= n
        total += result
    return total

sample_result_2 = cephalopod_math_homework(sample_input)
with open('aoc25_06_input.txt') as f:
    result_2 = cephalopod_math_homework(f.read())

print(f"The result for part 2 on the sample input is {sample_result_2}.")
print(f"The second result is {result_2}.")
