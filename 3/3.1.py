file = open("input.txt", "r")
lines = file.readlines()
is_valid = 0
for line in lines:
    line = line.replace('\n', '')
    triangle = line.split(" ")
    tmp = [];
    for t in triangle:
        if t != '':
            tmp.append(int(t))
    tmp.sort()
    if (tmp[0] + tmp[1] > tmp[2]):
        is_valid += 1
print(is_valid)