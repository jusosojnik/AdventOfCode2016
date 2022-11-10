num_of_elves = 3001330

dict = []
for i in range(num_of_elves):
    dict.append([1, i])

i = 0
while True:
    c = i % len(dict)
    i = c
    print(i, c, len(dict))
    # print(dict)
    if len(dict) == 1:
        break 
    middle = len(dict)//2
    middle += c
    middle %= len(dict)
    # print(middle)
    dict[c][0] += dict[middle][0]
    dict.pop(middle)
    if middle < c:   
        pass
    else:
        i += 1
    # input()

print(dict[0][1] + 1)