import codecs
from binascii import unhexlify
input1 = unhexlify("1c0111001f010100061a024b53535009181c")
input2 = unhexlify("686974207468652062756c6c277320657965")
expectedResult = unhexlify("746865206b696420646f6e277420706c6179")


def bxor(a, b):
    return [a ^ b for a, b in zip(a, b)]


assert bxor(input1, input2) == expectedResult
