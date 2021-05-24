import hashlib

id = "reyedfim"
index = 0
good_hash = True
password = ["", "", "", "", "", "", "", ""]
position = 0
for i in range(8):
    while True:
        good_hash = True
        hash = id + str(index)
        hash = hash.encode()
        result = hashlib.md5(hash).hexdigest()
        for j in range(5):
            if result[j] != '0':
                good_hash = False
                break
        index += 1
        if good_hash:
            if not result[5].isalpha():
                position = int(result[5])
                if position < 8 and password[position] == "":
                    password[position] = result[6]
                    break
password = "".join(password)
print(password)