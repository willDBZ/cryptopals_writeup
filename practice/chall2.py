from binascii import unhexlify
ct1 = unhexlify("1c0111001f010100061a024b53535009181c")
ct2 = unhexlify("686974207468652062756c6c277320657965")
result = unhexlify("746865206b696420646f6e277420706c6179")


def bxor(a, b):
    return bytes([a ^ b for a, b in zip(a, b)])


assert result == bxor(ct1, ct2)
