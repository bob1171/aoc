with open('./6.txt', 'r') as f:
    input = f.read()
    
p1 = 0
p2 = 0

from collections import defaultdict

grid = defaultdict(str)

height = len(input.splitlines())
width = len(input.splitlines()[0])

for y in range(height):
    for x in range(width):
        grid[(x,y)] = input.splitlines()[y][x]

