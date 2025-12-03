# Advent of Code 2025
# Day 03
# https://adventofcode.com/2025/day/3

year = 2025
day = 3
print(f"It's day {day} for Advent of Code {2025}, let's go!")

###############################################################
# Sample playground

sample_input = '''987654321111111
811111111111119
234234234234278
818181911112111'''

sample_result_1 = 0
result_1 = 0
sample_result_2 = 0
result_2 = 0

#print(sample_result_1)
#print(sample_result_2)
#quit()

###############################################################
# First part

with open('aoc25_03_input.txt') as f:
    for line in f:
        line = line.strip('\n') # before, line still includes the '\n' at the end
        l = len(line)
        if l < 2:
            continue

        i = 0
        x = int(line[i])

        for k, x_k in enumerate(line):
            if k < l-1 and int(x_k) > x:
                x = int(x_k)
                i = k
        j = i+1
        y = int(line[j])

        for y_k in line[j:-1]:
            if int(y_k) > y:
                y = int(y_k)

        result_1 += (10*x + y)

print(f"The first result is {result_1}.")
#quit()

###############################################################
# Second part: 12-digit substring with largest integer value

with open('aoc25_03_input.txt') as f:
    for line in f:
        line = line.strip('\n')
        l = len(line)
        #print(l)
        joltage = 0
        digits = [[i, i, int(line[i])] for i in range(12)]

        for i in range(12):
            j = digits[i][1]
            for k in range(j, l-(12-i)+1):
                x = int(line[k])
                if x > digits[i][-1]:
                    digits[i][-1] = x
                    digits[i][1] = k
                    for m in range(1, 12-i):
                        digits[i+m][1] = k+m
                        digits[i+m][-1] = int(line[k+m])

        for i, _, x_i in digits:
            joltage += (x_i * 10**(11-i))
        result_2 += joltage

print(f"The second result is: {result_2}.")