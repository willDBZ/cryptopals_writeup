import codecs
hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
expectedVal = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"


def hexToBase64(hex):
    inBytes = codecs.decode(hex, 'hex')
    b64 = codecs.encode(inBytes, 'base64').decode()[:-1]
    return b64


print(hexToBase64(hex))
assert expectedVal == hexToBase64(hex)
