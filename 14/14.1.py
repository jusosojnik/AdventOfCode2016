import hashlib
import re

input = "jlmsuwbz"
i = 0
key = 0
while True:
    print(i)
    t1 = input + str(i)
    md51 = hashlib.md5(t1.encode())
    s1 = md51.hexdigest()
    for e in range(2016):
        md51 = hashlib.md5(s1.encode())
        s1 = md51.hexdigest()
    matcher1 = re.compile(r'(\w)\1{2,}')
    m1 = [match.group() for match in matcher1.finditer(s1)]
    if m1:
        # print(m1, i)
        # break
        l = m1[0][0]
        for j in range(1, 1001):
            t2 = input + str(i + j)
            md52 = hashlib.md5(t2.encode())
            s2 = md52.hexdigest()
            rgx = l + '{5,}'
            for e in range(2016):
                md52 = hashlib.md5(s2.encode())
                s2 = md52.hexdigest()
            matcher2 = re.compile(rgx)
            m2 = [match.group() for match in matcher2.finditer(s2)]
            if m2:
                print(m1, i)
                print(m2, j + i)
                key += 1
                break
        if key == 64:
            break
        
    i += 1
