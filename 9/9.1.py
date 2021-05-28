import re

file = open("input.txt", "r")
lines = file.readlines()

count = 0

for line in lines:
    answer = ""
    while True:
        result = re.findall(r"(\(\d+x\d+\))", line)
        if len(result) == 0:
            break
        result = result[0]
        nums = re.findall(r"\d+", result)
        start_pos = line.find(result) + len(result)
        substr = line[start_pos:int(nums[0]) + start_pos]
        new_string = ""
        for i in range(int(nums[1]) - 1):
            new_string += substr
        new_start_pos = line.find(result) + int(nums[0]) * int(nums[1])
        answer += line.replace(result, new_string, 1)[:new_start_pos]
        line = line.replace(result, new_string, 1)
        line = line[new_start_pos:]
    print((answer + line).replace(" ", ""))
    print(len(answer))
    count += len(answer + line)
print(count)