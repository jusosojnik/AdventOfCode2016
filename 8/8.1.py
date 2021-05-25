import re
import copy

file = open("input.txt", "r")
lines = file.readlines()

grid = []

def gen_grid(x, y):
    for i in range(y):
        grid.append([])
        for j in range(x):
            grid[i].append('.')

gen_grid(50, 6)

for line in lines:
    result = re.findall(r"\d+", line)
    c1 = int(result[0])
    c2 = int(result[1])
    if 'rect' in line:
        for i in range(c2):
            for j in range(c1):
                grid[i][j] = '#'
    elif 'column' in line:
        for j in range(c2):
            tmp = copy.deepcopy(grid)
            for i in range(len(grid)):
                if i == 0:
                    grid[i][c1] = tmp[len(grid) - 1][c1]
                else:    
                    grid[i][c1] = tmp[i - 1][c1]
    elif 'row' in line:
        for j in range(c2):
            tmp = copy.deepcopy(grid)
            for i in range(len(grid[0])):
                if i == 0:
                    grid[c1][i] = tmp[c1][len(grid[0]) - 1]
                else:
                    grid[c1][i] = tmp[c1][i -1]
for e in grid:
    print(e)
count = 0
for e in grid:
    for i in e:
        if i == '#':
            count += 1
print(count)
    