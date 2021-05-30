import re

file = open("input.txt", "r")
lines = file.readlines()

def recursion(str, num):
    global count
    while True:
        results = re.findall(r"(\(\d+x\d+\))", str)
        if len(results) == 0:
            break
        count -= (len(results[0]) * num)
        nums = re.findall(r"\d+", results[0])
        count += ((int(nums[0]) * (int(nums[1]) - 1)) * num)
        start_pos = str.find(results[0]) + len(results[0])
        substr = str[start_pos:int(nums[0]) + start_pos]
        recursion(substr, int(nums[1]) * num)
        str = str.replace(results[0], "", 1)
        str = str.replace(substr, "", 1)

for line in lines:
    count = len(line)
    recursion(line, 1)
print(count)