input = ".^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^"
rows = 400000

safe_tiles = input.count('.')

for j in range(rows - 1):
    row = ""
    print(input, j)
    for i in range(len(input)):
        l = False
        c = False
        r = False

        if i != 0:
            if input[i - 1] == '^':
                l = True
        if i != len(input) - 1:
            if input[i + 1] == '^':
                r = True

        if input[i] == '^':
                c = True

        if (c and l and r) or (not c and not l and not r) or (c and not l and not r) or (not c and l and r):
            safe_tiles += 1
            row += '.'
        else:
            row += '^'

    input = row
print(input)
print(safe_tiles)