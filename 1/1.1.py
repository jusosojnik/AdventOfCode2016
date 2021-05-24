orientation = 0
x = 0
y = 0
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
    elif orientation == 1:
        x += dist
    elif orientation == 2:
        y -= dist
    elif orientation == 3:
        x -= dist

with open('input.txt', 'r') as file:
    data = file.read().replace('\n', '')

instructions = data.split(", ")

for instruction in instructions:
    if instruction[0] == 'R':
        change_orientation(instruction[0])
        change_coordinates(int(instruction[1:len(instruction)]))
    elif instruction[0] == 'L':
        change_orientation(instruction[0])
        change_coordinates(int(instruction[1:len(instruction)]))


distance = abs(x) + abs(y)

print(distance)