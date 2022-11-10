file1 = open('input.txt', 'r')
Lines = file1.readlines()


lines = []
for line in Lines:
    line = line.strip().split('-')
    lines.append([int(line[0]), int(line[1])])
lines = sorted(lines)
start = lines[0][0]
end = lines[0][1]

count = 0
for i in range(1, len(lines)):
    if lines[i][0] - 1 > end:
        count += lines[i][0] - 1 - end
        if lines[i][1] > end:
            end = lines[i][1]
    elif lines[i][1] > end:
            end = lines[i][1]

print(count + 4294967295 - end)
