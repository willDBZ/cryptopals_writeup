from binascii import unhexlify
from binascii import Error

charsCodeList = [i for i in range(ord('a'), ord('z'))] + [ord(' ')]


def calculateScore(val):
    return sum([a in charsCodeList for a in val])


def bxor(a, b):
    return bytes([a ^ b for a, b in zip(a, b)])


def calculateRatio(val):
    return calculateScore(val) / len(val)


def decryptedOneByteXor(ct):
    maxScore = 0
    for i in range(1, 255):
        key = bytes([i]) * len(ct)
        res = bxor(ct, key)
        score = calculateScore(res)
        if maxScore < score:
            maxScore = score
            ratio = calculateRatio(res)
            decrypted = {'key': chr(i), 'message': res,
                         'score': score, 'ratio': ratio}
    return decrypted


def isOneByteXor(line):
    return decryptedOneByteXor(line)


file = open('4.txt', 'r')
Lines = file.readlines()
max = 0

for line in Lines:
    try:
        res = isOneByteXor(unhexlify(line[:-1]))
    except Error:
        print(line)
    if res['ratio'] > max:
        max = res['ratio']
        bestVal = res
print(bestVal)
