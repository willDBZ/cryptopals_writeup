from binascii import unhexlify


def bxor(a, b):
    return bytes([a ^ b for a, b in zip(a, b)])


def getScore(val):
    return sum([c in englishChars for c in val])


englishChars = list(range(ord('a'), ord('z'))) + [ord(' ')]

ciphertext = unhexlify(
    "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

max = 0
maxKey = None
maxMessage = None
for i in range(1, 255):
    key = bytes([i]) * len(ciphertext)
    try:
        res = bxor(ciphertext, key)
        score = getScore(res)
        if (score > max):
            max = score
            maxKey = key
            maxMessage = res
    except UnicodeDecodeError:
        print('oops')

print(f'max:{max}, maxKey:{maxKey}, maxMessage: {maxMessage}')
