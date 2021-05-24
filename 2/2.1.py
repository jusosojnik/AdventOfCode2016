f = open('input.txt', 'r')
instructions = f.readlines()
code = ""
pos = 5
for instruction in instructions:
    for i in range(len(instruction)):
        if instruction[i] == 'R':
            if pos != 3 and pos != 6 and pos != 9:
                pos += 1
        elif instruction[i] == 'L':
            if pos != 1 and pos != 4 and pos != 7:
                pos -= 1
        elif instruction[i] == 'U':
            if pos != 1 and pos != 2 and pos != 3:
                pos -= 3 
        elif instruction[i] == 'D':
            if pos != 7 and pos != 8 and pos != 9:
                pos += 3
    code += str(pos)
print(code)