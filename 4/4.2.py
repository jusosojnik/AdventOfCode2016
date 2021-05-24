import re

file = open("input.txt", "r")
lines = file.readlines()

for line in lines:
    result = re.findall(r"^[^\d]+", line)[0]
    id = int(re.search(r"[0-9]+", line)[0])
    result = list(result.replace("-", " "))
    for i in range(id):
        for i in range(len(result)):
            if (result[i] == 'z'):
                result[i] = 'a'
            elif (result[i] == ' '):
                continue
            else:
                result[i] = chr(ord(result[i]) + 1)
    result = "".join(result)
    print(result)
    print(id)