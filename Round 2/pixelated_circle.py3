# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 2 - Problem B. Pixelated Circle
# https://codingcompetitions.withgoogle.com/codejam/round/00000000008778ec/0000000000b158f7
#
# Time:  O(R)
# Space: O(1)
#

from math import cos, pi

def draw_circle_filled(R):
    return sum(2*int(((R+0.5)**2-x**2)**0.5)+1 for x in range(1, R+1))*2+(2*R+1)

def draw_circle_perimeter(r):
    x1, x2 = int(r*cos(pi/4)), int(r*cos(pi/4))+1
    y1, y2 = round((r**2-x1**2)**0.5), round((r**2-x2**2)**0.5)
    candidates = [(x1, y1), (x2, y2)]
    x, y = min(((x, y) for x, y in candidates if x <= y), key=lambda x:x[1]-x[0])
    return 2*x+1-int(x == y)

def draw_circle_filled_wrong(R):
    return sum(draw_circle_perimeter(r) for r in range(1, R+1))*4+1

def pixelated_circle():
    R = int(input())
    return draw_circle_filled(R)-draw_circle_filled_wrong(R)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, pixelated_circle()))
