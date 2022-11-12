inputxt = [*'efghdabc']

file1 = open('input.txt', 'r')
Lines = file1.readlines()


lines = []
for line in Lines:
    lines.append(line.strip().split(' '))


def leftrotate(s, d):
    tmp = s[d : ] + s[0 : d]
    return tmp
   

def rightrotate(s, d):
   return leftrotate(s, len(s) - d)


def convert(s):
    str1 = ""
    return(str1.join(s))


for line in lines:
    print(inputxt)
    print(line)
    if line[0] == 'swap':
        if line[1] == 'position':
            t = inputxt[int(line[2])]
            inputxt[int(line[2])] = inputxt[int(line[5])]
            inputxt[int(line[5])] = t
        elif line[1] == 'letter':
            x = inputxt.index(line[2])
            y = inputxt.index(line[5])
            t = inputxt[x]
            inputxt[x] = inputxt[y]
            inputxt[y] = t
    elif line[0] == 'move':
        t = inputxt.pop(int(line[2]))
        inputxt.insert(int(line[5]), t)
    elif line[0] == 'rotate':
        if line[1] == 'left':
            inputxt = leftrotate(inputxt, int(line[2]))
        elif line[1] == 'right':
            inputxt = rightrotate(inputxt, int(line[2]))
        elif line[1] == 'based':
            x = inputxt.index(line[6])
            r = x + 1
            if x >= 4:
                r += 1
            inputxt = rightrotate(inputxt, r)
            
    elif line[0] == 'reverse':
        t = inputxt[int(line[2]):int(line[4]) + 1]
        t.reverse()
        inputxt[int(line[2]):int(line[4]) + 1] = t

print(convert(inputxt))