import hashlib

id = "reyedfim"
index = 0
password = ""
good_hash = True
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
            password += result[5]
            break
print(password)