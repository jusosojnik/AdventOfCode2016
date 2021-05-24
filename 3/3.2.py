file = open("input.txt", "r")
lines = file.readlines()
columns = []
is_valid = 0
for i in range(3):
    tmp = []
    j = 0
    for line in lines:
        j += 1
        if j == 4:
            tmp = []
            j = 1
        tmp.append(line.split()[i])
        if tmp not in columns:
            columns.append(tmp)
print(len(columns))
for e in columns:
    #print(e)
    e.sort()
    if int(e[0]) + int(e[1]) > int(e[2]) and int(e[0]) + int(e[2]) > int(e[1]) and int(e[1]) + int(e[2]) > int(e[0]):
        print(e)
        is_valid += 1
print(is_valid)
#100 200 4