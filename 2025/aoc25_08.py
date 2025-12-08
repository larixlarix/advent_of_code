# Advent of Code 2025
# Day 08
# https://adventofcode.com/2025/day/8

year = 2025
day = 8
print(f"It's day {day} for Advent of Code {year}, let's go!")

###############################################################
# Sample playground

sample_result_1 = 1
result_1 = 1
sample_result_2 = 1
result_2 = 1

# DADDLE, YOODLE, YAY

sample_input = '''\
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''

def dist_sq(p0, p1): 
    x0, y0, z0 = p0
    x1, y1, z1 = p1
    diff = [x1-x0, y1-y0, z1-z0]
    return sum([v**2 for v in diff])

#with open('aoc25_07_input.txt') as f:
    for line in f:
        first_line = line.rstrip('\n')
        break


pos = []
with open('aoc25_08_input.txt') as f:
    input_lines=f.read().split('\n')
#input_lines = sample_input.split('\n')
for line in input_lines:
    pos.append([int(i) for i in line.rstrip().split(',')])

n = len(pos)
#print(n)

distances_sq = dict()
for i in range(n):
    for j in range(i+1, n):
        distances_sq[(i, j)] = dist_sq(pos[i], pos[j])

distances_sq = sorted(distances_sq.items(), key=lambda item: item[1])
#print(distances_sq)

n_conns = 1000
n_circs = 3
connections = [item[0] for item in distances_sq[:n_conns]] 
circuits =  [{i} for i in range(n)]

for conn in connections:
    #print(conn)
    i, j = conn
    circ_update = set(conn)
    remove_circs = []
    for circ in circuits:
        if not circ.isdisjoint(circ_update):
            circ_update.update(circ)
            remove_circs.append(circ)
            #print(f"Removing {circ}")
    circuits.append(circ_update)
    for circ in remove_circs:
        circuits.remove(circ)
    #print(conn, circ_update, circuits)

sorted_circuit_lengths = sorted([len(circ) for circ in circuits], reverse=True)
for i in sorted_circuit_lengths[:n_circs]:
    #sample_result_1 *= i
    result_1 *= i

#print(f"The result on the sample input is {sample_result_1}.")
#quit()

###############################################################
# First part: connect 1000 shortest connections

print(f"The first result is {result_1}.")
#quit()

###############################################################
# Second part: connect until there is only one circuit

connections_all = [item[0] for item in distances_sq]
circuits =  [{i} for i in range(n)]
for conn in connections_all:
    #print(conn)
    i, j = conn
    circ_update = set(conn)
    remove_circs = []
    for circ in circuits:
        if not circ.isdisjoint(circ_update):
            circ_update.update(circ)
            remove_circs.append(circ)
    circuits.append(circ_update)
    for circ in remove_circs:
        circuits.remove(circ)
    if len(circuits) == 1:
        result_2 = pos[i][0]*pos[j][0]
        break

#print(f"The result for part 2 on the sample input is {sample_result_2}.")
print(f"The second result is {result_2}.")
