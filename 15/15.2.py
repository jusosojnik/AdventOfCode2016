import copy

discs = {'1' : [13, 10],
         '2' : [17, 15],
         '3' : [19, 17],
         '4' : [7, 1],
         '5' : [5, 0],
         '6' : [3, 1],
         '7' : [11, 0]}

time = 0
while True:
    discs_copy = copy.deepcopy(discs)
    win = True
    for i in range(1, 8):
        state = discs_copy[str(i)][1]
        if state + i + time >= discs_copy[str(i)][0]:
            discs_copy[str(i)][1] = (state + i + time) % discs_copy[str(i)][0]
            if discs_copy[str(i)][1] != 0:
                win = False
        else:
            discs_copy[str(i)][1] += (i + time)
            win = False
    print(discs_copy)
    if win:
        print(time)
        break
    time += 1