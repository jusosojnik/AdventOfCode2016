num_of_elves = 3001330

dict = {}
for i in range(num_of_elves):
    dict[str(i)] = 1

i = 0
greedyElf = False
while not greedyElf:
    print(i)
    c = i % num_of_elves
    if dict[str(c)] == 0:
        # print(dict, c)
        i += 1
        continue

    greedyElf = True

    for j in range(c + 1, c + 1 + num_of_elves - 2):
        n = j % num_of_elves
        if dict[str(n)] > 0:
            dict[str(c)] += dict[str(n)]
            dict[str(n)] -= dict[str(n)]
            greedyElf = False
            break

    # print(dict, c)
    i += 1

for j in range(num_of_elves):
    if dict[str(j)] > 0:
        print("Result", j + 1)
        break