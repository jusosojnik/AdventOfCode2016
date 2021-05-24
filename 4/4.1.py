import re

file = open("input.txt", "r")
lines = file.readlines()

sum = 0

for line in lines:
    result = re.findall(r"[^\[\]]+", line)
    id = int(re.search(r"[0-9]+", line)[0])
    first = result[0]
    checksum = result[1]
    chars = [0, 0, 0, 0, 0]
    is_valid = True
    for i in range(len(checksum)):
        for c in first:
            if checksum[i] == c:
                chars[i] += 1
    for c in chars:
        if c == 0:
            is_valid = False
            break
    e = 1
    while e < len(chars):
        if not (chars[e - 1] >= chars[e]):
            is_valid = False
            break

        if(chars[e - 1] == chars[e]):
            if not (checksum[e - 1] < checksum[e]):
                is_valid = False
                break
        e += 1
    if is_valid:
        sum += id
print(sum)

