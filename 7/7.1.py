import re

file = open("input.txt", "r")
lines = file.readlines()

support_count = 0

for line in lines:
    is_valid = False
    hyper_seq = re.findall(r"(?<=\[)(.*?)(?=\])", line)
    p1 = re.findall(r"(.*?)(?=\[)", line)[0]
    p2 = re.findall(r"([^\]]+$)", line)[0]
    p3 = re.findall(r"(?<=\])(.*?)(?=\[)", line)
    for i in range(len(p1) - 3):
        i += 3
        if p1[i] == p1[i - 3] and p1[i - 1] == p1[i - 2] and p1[i] != p1[i - 1]:
            is_valid = True
            break
    for i in range(len(p2) - 3):
        i += 3
        if p2[i] == p2[i - 3] and p2[i - 1] == p2[i - 2] and p2[i] != p2[i - 1]:
            is_valid = True
            break
    for j in range(len(p3)): 
        for i in range(len(p3[j]) - 3):
            i += 3
            if p3[j][i] == p3[j][i - 3] and p3[j][i - 1] == p3[j][i - 2] and p3[j][i] != p3[j][i - 1]:
                is_valid = True
                break
    for j in range(len(hyper_seq)): 
        for i in range(len(hyper_seq[j]) - 3):
            i += 3
            if hyper_seq[j][i] == hyper_seq[j][i - 3] and hyper_seq[j][i - 1] == hyper_seq[j][i - 2] and hyper_seq[j][i] != hyper_seq[j][i - 1]:
                is_valid = False
                break
    if is_valid:
        support_count += 1
print(support_count)