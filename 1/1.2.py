orientation = 0
x = 0
y = 0
grid = [[0, 0]]

def change_orientation(x):
    global orientation
    if x == 'R':
        if orientation == 3: 
            orientation = 0 
        else:
            orientation += 1
    elif x == 'L':
        if orientation == 0: 
            orientation = 3 
        else: 
            orientation -= 1


def change_coordinates(dist):
    global x, y
    if orientation == 0:
        y += dist
        k = len(grid)
        for i in range(dist):
            if [grid[k - 1][0], grid[k - 1][1] + i + 1] not in grid:
                grid.append([grid[k - 1][0], grid[k - 1][1] + i + 1])
    elif orientation == 1:
        x += dist
        k = len(grid)
        for i in range(dist):
            if  [grid[k - 1][0] + i  + 1, grid[k - 1][1]] not in grid:
                grid.append([grid[k - 1][0] + i  + 1, grid[k - 1][1]])
    elif orientation == 2:
        y -= dist
        k = len(grid)
        for i in range(dist):
            if [grid[k - 1][0], grid[k - 1][1] - i - 1] not in grid:
                grid.append([grid[k - 1][0], grid[k - 1][1] - i - 1])
    elif orientation == 3:
        x -= dist
        k = len(grid)
        for i in range(dist):
            if [grid[k - 1][0] - i - 1, grid[k - 1][1]] not in grid:
                grid.append([grid[k - 1][0] - i - 1, grid[k - 1][1]])
    
    
def check_crossing(dist):
    global x, y
    tmp = []
    if orientation == 0:
        k = len(grid)
        for i in range(dist):
            tmp.append([grid[k - 1][0], grid[k - 1][1] + i + 1])
    elif orientation == 1:
        k = len(grid)
        for i in range(dist):
            tmp.append([grid[k - 1][0] + i  + 1, grid[k - 1][1]])

    elif orientation == 2:
        k = len(grid)
        for i in range(dist):
            tmp.append([grid[k - 1][0], grid[k - 1][1] - i - 1])
    elif orientation == 3:
        k = len(grid)
        for i in range(dist):
            tmp.append([grid[k - 1][0] - i - 1, grid[k - 1][1]])

    for e in tmp:
        if (e in grid):
            y = e[1]
            x = e[0]
            return True

    return False

with open('input.txt', 'r') as file:
    data = file.read().replace('\n', '')

instructions = data.split(", ")
locations = [[0, 0]]

for instruction in instructions:
    if instruction[0] == 'R':
        change_orientation(instruction[0])
        if len(grid) != 0:
            if(check_crossing(int(instruction[1:len(instruction)]))):
                break;
        change_coordinates(int(instruction[1:len(instruction)]))
    elif instruction[0] == 'L':
        change_orientation(instruction[0])
        if len(grid) != 0:
            if(check_crossing(int(instruction[1:len(instruction)]))):
                break;
        change_coordinates(int(instruction[1:len(instruction)]))

distance = abs(x) + abs(y)

print(distance)