file1 = open('input.txt', 'r')
Lines = file1.readlines()

lines = []

for line in Lines:
    lines.append(line.strip().split(" "))

start_value = 0
done = False
treshold = 500
while True:
    reg =  {'a': start_value,
            'b': 0,
            'c': 0,
            'd': 0}

    signal = ""
    c = '0'
    i = 0
    
    while i < len(lines):
        line = lines[i]

        if line[0] == 'cpy':
            if not line[2].lstrip("-").isdigit():
                if line[1].lstrip("-").isdigit():
                    reg[line[2]] = int(line[1])
                else:
                    reg[line[2]] = reg[line[1]]
        elif line[0] == 'inc':
            reg[line[1]] += 1
        elif line[0] == 'dec':
            reg[line[1]] -= 1
        elif line[0] == 'jnz':
            if line[1].lstrip("-").isdigit():
                if int(line[1]) != 0:
                    if line[2].lstrip("-").isdigit():
                        i += int(line[2]) - 1
                    else:
                        i += reg[line[2]] - 1
            else:
                if reg[line[1]] != 0:
                    i += int(line[2]) - 1
        elif line[0] == 'tgl':
            new_i = i
            if line[1].lstrip("-").isdigit():
                new_i += int(line[1])
            else:
                new_i += reg[line[1]]
            if new_i < len(lines) and new_i > -1:
                if len(lines[new_i]) == 2:
                    if lines[new_i][0] == "inc":
                        lines[new_i][0] = "dec"
                    else:
                        lines[new_i][0] = "inc"
                elif len(lines[new_i]) == 3:
                    if lines[new_i][0] == "jnz":
                        lines[new_i][0] = "cpy"
                    else:
                        lines[new_i][0] = "jnz"
        elif line[0] == 'mul':
            print(reg[line[2]], reg[line[3]])
            reg[line[1]] = reg[line[2]] * reg[line[3]]
        elif line[0] == 'add':
            reg[line[1]] += reg[line[2]]
        elif line[0] == 'out':
            _signal = ""
            if line[1].lstrip("-").isdigit():
                _signal = line[1]
            else:
                _signal = str(reg[line[1]])
            
            signal += _signal
            
            if _signal != c:
                break
            elif c == "0":
                c = "1"
            else:
                c = "0"
            
            if len(signal) > treshold:
                done = True
                break

        i += 1
    if done:
        print(f"Answer is {start_value}")
        break
    start_value += 1