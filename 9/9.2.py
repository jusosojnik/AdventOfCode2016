import re

file = open("input.txt", "r")
lines = file.readlines()

def recursion(substr, num):
    global tmp_count, line
    while True:
        print("##################################################")
        print(substr)
        print(tmp_count)
        results = re.findall(r"(\(\d+x\d+\))", substr)
        if len(results) == 0:
                break
        result = results[0]
        tmp_count -= len(result) * num
        print(tmp_count)
        tmp_nums = re.findall(r"\d+", result)
        tmp_count += (int(tmp_nums[0]) * (int(tmp_nums[1]) - 1)) * num
        print(tmp_count)
        start_pos = substr.find(result) + len(result)
        tmp_substr = substr[start_pos:int(tmp_nums[0]) + start_pos]
        print(tmp_substr)
        print(tmp_nums)
        line = line.replace(result, "", 1)
        line = line.replace(tmp_substr, "", 1)
        print(line)
        substr = substr.replace(result, "", 1)
        substr = substr.replace(tmp_substr, "", 1)
        #1677737001
        #2535549295
        #1575761386
        print(tmp_count)
        print(substr)
        tmp_substr = tmp_substr.replace(result, "", 1)

        recursion(tmp_substr, int(int(tmp_nums[1]) * num))
        for r in results:
            if r in tmp_substr:
                substr = substr.replace(r, "", 1)
        
    #print(tmp_count)
    #print("GREMO VN")

count = 0

for line in lines:
    line = line.replace("\n", "")
    print(line)
    tmp_count = len(line)
    print(tmp_count)
    results = re.findall(r"(\(\d+x\d+\))", line)
    while True:
        print("KKKKKKKKKKKKKKKKKKKKKKKKK")
        results = re.findall(r"(\(\d+x\d+\))", line)
        if len(results) == 0:
            break
        result = results[0]
        print(result)
        tmp_count -= len(result)
        nums = re.findall(r"\d+", result)
        tmp_count += int(nums[0]) * (int(nums[1]) - 1)
        start_pos = line.find(result) + len(result)
        substr = line[start_pos:int(nums[0]) + start_pos]
        print(substr)
        line = line.replace(result, "", 1)
        line = line.replace(substr, "", 1)
        print(line)
        print(tmp_count)
        print(substr)
        print(results)
        recursion(substr, int(nums[1]))
        print("PA SMO ZUNI")
        print(tmp_count)
        print(substr)
        print(line)
        # while True:
        #     results = re.findall(r"(\(\d+x\d+\))", substr)
        #     print(tmp_count)
        #     if len(results) == 0:
        #         break
        #     result = results[0]
        #     print(result)
        #     tmp_count -= len(result) * int(nums[1])
        #     print(tmp_count)
        #     num = int(nums[1])
        #     nums = re.findall(r"\d+", result)
        #     print((int(nums[0]) * (int(nums[1]) - 1)) * num)
        #     tmp_count += (int(nums[0]) * (int(nums[1]) - 1)) * num 
        #     line = line.replace(result, "", 1)
        #     substr = substr.replace(result, "", 1)
    print(tmp_count)
    count += tmp_count
    break
print(count)

# count = 0

# for line in lines:
#     answer = ""
#     results = re.findall(r"(\(\d+x\d+\))", line)
#     while True:
#         results = re.findall(r"(\(\d+x\d+\))", line)
#         if len(results) == 0:
#             break
#         result = results[0]
#         nums = re.findall(r"\d+", result)
#         start_pos = line.find(result) + len(result)
#         substr = line[start_pos:int(nums[0]) + start_pos]
#         new_string = ""
#         for i in range(int(nums[1]) - 1):
#             new_string += substr
#         new_start_pos = line.find(result) + int(nums[0]) * int(nums[1])
#         line = line.replace(result, new_string, 1)
#     print(len(line))
#     print(line)
#     count += len(line)
# print(count)

