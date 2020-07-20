from binascii import unhexlify

ct = unhexlify(
    "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")


def bxor(a, b):
    return bytes([a ^ b for a, b in zip(a, b)])


charsCodeList = [i for i in range(ord('a'), ord('z'))] + [ord(' ')]


def calculateScore(val):
    return sum([a in charsCodeList for a in val])


def decryptedOneByteXor(ct):
    maxScore = 0
    for i in range(1, 255):
        key = bytes([i]) * len(ct)
        res = bxor(ct, key)
        score = calculateScore(res)
        if maxScore < score:
            maxScore = score
            decrypted = {'key': chr(i), 'message': res}
    return decrypted


print(decryptedOneByteXor(ct))
