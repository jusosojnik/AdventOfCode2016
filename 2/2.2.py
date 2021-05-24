f = open('input.txt', 'r')
instructions = f.readlines()
code = ""
pos = 5
for instruction in instructions:
    for i in range(len(instruction)):
        if instruction[i] == 'R':
            if pos != 1 and pos != 4 and pos != 9 and pos != 12 and pos != 13:
                pos += 1
        elif instruction[i] == 'L':
            if pos != 1 and pos != 2 and pos != 5 and pos != 10 and pos != 13:
                pos -= 1
        elif instruction[i] == 'U':
            if pos != 1 and pos != 2 and pos != 5 and pos != 4 and pos != 9:
                if pos == 13: pos -= 2
                elif pos > 9: pos -= 4
                elif pos > 4: pos -= 4
                elif pos < 5: pos -= 2 
        elif instruction[i] == 'D':
            if pos != 5 and pos != 10 and pos != 13 and pos != 12 and pos != 9:
                if pos == 1: pos += 2
                elif pos < 5: pos += 4
                elif pos < 10: pos += 4
                elif pos > 9: pos += 2 
    if pos == 10:
        code += "A"
    elif pos == 11:
        code += "B"
    elif pos == 12:
        code += "C"
    elif pos == 13:
        code += "D"
    else:
        code += str(pos)
print(code)