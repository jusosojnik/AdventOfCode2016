input = "01111010110010011"
diskLenght = 35651584

data = input

while len(data) < diskLenght:
    a = data
    b = a
    b = b[::-1]
    b = b.replace('1', '2')
    b = b.replace('0', '1')
    b = b.replace('2', '0')
    a += '0' + b
    data = a

data = data[:diskLenght]
print(data)
checksum = ""
while len(checksum) % 2 == 0:
    checksum = ""
    for i in range(0, len(data), 2):
        if data[i] == data[i + 1]:
            checksum += '1'
        else:
            checksum += '0'
    data = checksum
    print(checksum)