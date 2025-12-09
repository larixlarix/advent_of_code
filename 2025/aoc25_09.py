# Advent of Code 2025
# Day 09
# https://adventofcode.com/2025/day9

year = 2025
day = 9
print(f"It's day {day} for Advent of Code {year}, let's go!")

###############################################################
# Sample playground

sample_result_1 = 1
result_1 = 1
sample_result_2 = 1
result_2 = 1

# DADDLE, YOODLE, YAY

print("Hello world!")
sample_input = '''\
7,1
11,1
11,7
9,7
9,4
2,4
2,3
7,3'''

#input_lines = sample_input.split('\n')
with open('aoc25_09_input.txt') as f:
    input_lines=f.read().split('\n')
pos = []
for line in input_lines:
    pos.append([int(i) for i in line.rstrip().split(',')])

n = len(pos)
from matplotlib.path import Path
path = Path(pos)

def minus(t0, t1):
    return [t1[0] - t0[0], t1[1]-t0[1]]

def det(t0, t1):
    a, b = t0
    c, d = t1
    return a*d - b*c

from shapely.geometry import Point, Polygon
polygon = Polygon(pos)

 
#print(path.contains_point((0,0)))
#quit()

def red_or_green(t):
    point = Point(*t)
    return polygon.contains(point) or polygon.touches(point)

#red_or_green((0,0))
#quit()

def area(t0, t1, part_2 = False):
    i, j = t0
    k, l = t1
    t2 = [i, l]
    t3 = [k, j]
    rect_area = max((i-k+1)*(j-l+1), (i-k+1)*(l-j+1), (k-i+1)*(j-l+1), (k-i+1)*(l-j+1))
    
    if not part_2:
        return rect_area

    print(f"Checking {arrea, t0, t1}", end = " ")
    if not (red_or_green(t2) and red_or_green(t3)):
        print("A.")#t0, t1, area)
        return 0
    
    for t4 in pos:
        x, y = t4
        if min(i,k) < x < max(i,k) and min(j,l) < y < max(j,l):
            print("B.", x, y)#t0, t1, area)
            return 0
    
    for z in range(min(i, k), max(i, k)+1):
        #print(i, k, min(i, k), max(i, k))
        if not red_or_green((z, j)):
            print("C", (z, j))
            return 0
        if not red_or_green((z, l)):
            print("C", (z, l))
            return 0

    for w in range(min(j, l), max(j, l)+1):
        if not red_or_green((i, w)):
            print("C", (i,w))
            return 0
        if not red_or_green((k, w)):
            print("C", (k,w))
            return 0
    print("Yikes.")
    return rect_area

#print(n)
areas = []
area_infos = []
#maximum = 0
for r in range(n):
    for s in range(r+1, n):
        A = area(pos[r], pos[s], part_2=False)
        areas.append(A)
        area_infos.append((A, pos[r], pos[s]))
        #if area(pos[r], pos[s], pos) > maximum:
        #    A = area(pos[r], pos[s], pos, part_2=True)
        #    if A > maximum:
        #        maximum = A
        #        print(f"Found new biggest rectangle with area {maximum} between corners {pos[r], pos[s]}.")

#result_2 = maximum

#print(f"The result on the sample input is {sample_result_1}.")
#quit()

###############################################################
# First part: 

result_1 = max(areas)
print(f"The first result is {result_1}.")
#quit()

###############################################################
# Second part: 
sorted_area_infs = sorted(area_infos, key=lambda x: -x[0])
B = result_1
count = -1
for area_info in sorted_area_infs[0:]:
    count += 1
    A, r0, r1 = area_info
    print(f'{count} Testing {area_info}, B-A = {B-A}', end= ' ')
    B = A
    A2 = area(r0, r1, part_2=True)
    print(A2)
    if A2 == A:
        result_2 = A2
        print(f"The second result is {result_2, r0, r1}.")
        break
        
print(f"For reference, the first result still is {result_1}.")
#print(areas_part_2)
#print(f"The result for part 2 on the sample input is {sample_result_2}.")
#print(f"The second result is {result_2}.")
