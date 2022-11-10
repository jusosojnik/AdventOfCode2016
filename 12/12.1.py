file1 = open('input.txt', 'r')
Lines = file1.readlines()

lines = []
check = False
for line in Lines:
    lines.append(line.strip())

reg =  {'a': 0,
        'b': 0,
        'c': 0,
        'd': 0}

i = 0
while i < len(lines):
    line = lines[i].split(" ")
    print(line)

    if line[0] == 'cpy':
        if line[1].isdigit():
            reg[line[2]] = int(line[1])
        else:
            reg[line[2]] = reg[line[1]]
    elif line[0] == 'inc':
        reg[line[1]] += 1
    elif line[0] == 'dec':
        reg[line[1]] -= 1
    elif line[0] == 'jnz':
        if line[1].isdigit():
            if int(line[1]) != 0:
                i += int(line[2]) - 1
        else:
            if reg[line[1]] != 0:
                i += int(line[2]) - 1
                
    i += 1

print(reg['a'])