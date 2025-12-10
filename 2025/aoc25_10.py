# Advent of Code 2025
# Day 10
# https://adventofcode.com/2025/day10

year = 2025
day = 10
print(f"It's day {day} for Advent of Code {year}, let's go!")

###############################################################
# Sample playground

sample_result_1 = 0
result_1 = 0
sample_result_2 = 0
result_2 = 0

# DADDLE, YOODLE, YAY
print("Hello world!")

sample_input = '''\
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}'''

#input_lines = sample_input.split('\n')
with open('aoc25_10_input.txt') as f:
    input_lines=f.read().split('\n')

def toggle(lights, switch):
    for i in switch:
        lights[i] = '#' if lights[i]=='.' else '.' 

from itertools import chain, combinations

def switch_seqs(switches):
    return chain.from_iterable(combinations(switches, r) for r in range(len(switches)+1))
    #return [combinations(switches, r) for r in range(len(switches)+1)]

for line in input_lines:
    indicator_lights_str = line.split()[0].rstrip(']').lstrip('[')
    n_lights = len(indicator_lights_str)
    lights_out = n_lights*['.']
    lights = n_lights*['.']
    switches = [eval(s) for s in line.split()[1:-1]]
    for i, s in enumerate(switches):
        if type(s) == int:
            switches[i] = (s,)
    joltages = line.split()[-1]
    #print(indicator_lights_str, ''.join(lights), switches, joltages)
    #print(''.join(lights)) 
    #toggle(lights, first_switch)
    #print(''.join(lights))
    #print()
    for switch_seq in switch_seqs(switches):
        lights = n_lights*['.']
        for switch in switch_seq:
            toggle(lights, switch)
            #print(''.join(lights))
        if ''.join(lights) == indicator_lights_str:
            #print('Hurray!', len(switch_seq))
            result_1 += len(switch_seq)
            break
#print(f"The result on the sample input is {sample_result_1}.")
#quit()

###############################################################
# First part: 

print(f"The first result is {result_1}.")
#quit()

###############################################################
# Second part: 
import numpy as np
from scipy.optimize import linprog


for line in input_lines: 
    switches = [eval(s) for s in line.split()[1:-1]]
    for i, s in enumerate(switches):
        if type(s) == int:
            switches[i] = (s,)
    joltages = eval(line.strip().split()[-1].lstrip('{').rstrip('}'))
    U = sum(list(joltages))
    joltage_arr = np.array(list(joltages))
    J = len(joltage_arr)
    S = len(switches)
    #print(U, J, S, joltage_arr)

    c = np.ones(S, dtype=np.int8)
    #print(c)
    A_eq = np.zeros((J, S), dtype=np.int8)
    for k, switch in enumerate(switches):
        for i in switch:
            A_eq[i][k] = 1

    #print(A_eq)
    optimal_switches = linprog(c, A_eq=A_eq, b_eq=joltage_arr, bounds=(0, U), integrality=1).x
    #print(optimal_switches)
    result_2 += np.sum(optimal_switches)
#print(f"The result for part 2 on the sample input is {sample_result_2}.")
print(f"The second result is {int(result_2)}.")
