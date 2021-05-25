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
    babs = []
    abas = []
    char1 = ''
    char2 = ''
    for j in range(len(hyper_seq)):
        for i in range(len(hyper_seq[j]) - 2):
            i += 2
            if hyper_seq[j][i] == hyper_seq[j][i - 2] and hyper_seq[j][i] != hyper_seq[j][i - 1]:
                char1 = hyper_seq[j][i]
                char2 = hyper_seq[j][i - 1]
                tmp = [char1, char2]
                babs.append(tmp)
    if char1 != '' and char2 != '':
        for i in range(len(p1) - 2):
            i += 2
            for e in babs:
                if p1[i] == e[1] and p1[i - 2] == e[1] and p1[i - 1] == e[0]:
                    is_valid = True
                    break
            if is_valid:
                break
        if not is_valid:
            for i in range(len(p2) - 2):
                i += 2
                for e in babs:
                    if p2[i] == e[1] and p2[i - 2] == e[1] and p2[i - 1] == e[0]:
                        is_valid = True
                        break
                if is_valid:
                    break
        if not is_valid:
            for j in range(len(p3)):
                for i in range(len(p3[j]) - 2):
                    i += 2
                    for e in babs:
                        if p3[j][i] == e[1] and p3[j][i - 2] == e[1] and p3[j][i - 1] == e[0]:
                            is_valid = True
                            break
                    if is_valid:
                        break
                if is_valid:
                    break
    if is_valid:
        support_count += 1
print(support_count)