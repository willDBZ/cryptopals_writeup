from binascii import unhexlify
from base64 import b64encode

hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
expectedResult = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"


def hexToBase64(ct):
    ct = unhexlify(ct)
    b64 = b64encode(ct)
    return b64


assert expectedResult == hexToBase64(hex)
