from collections import Counter

file = open("input.txt", "r")
lines = file.readlines()
columns = []
message = ""
for x in range(len(lines[0]) - 1):
    columns.append([])
for line in lines:
    for i in range(len(columns)):
        columns[i].append(line[i])
for column in columns:
    message += Counter(column).most_common()[0][0]
print(message)
