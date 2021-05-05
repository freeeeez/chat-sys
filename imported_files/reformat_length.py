def _16_bit_len(word):
    for i in range(len(word), 16):
        word += '0'
    return word


def _original_len(word):
    word = word[::-1]
    l = list(word)
    i = 0
    while True:
        if l[i] == '0':
            del l[i]
        else:
            break
    word = ''.join(l)
    return word[::-1]


def client_key_transfer(key):  # key is the form of list in hexadecimal
    return ' '.join(key)


def client_key_receive(key):  # key is the form of string
    return key.split(' ')


"""
a=_16_bit_len('ABCD')
print(a)
a=_original_len(a)
print(a)

a = client_key_transfer(['000110010100110011010000011100101101111010001100', '010001010110100001011000000110101011110011001110', '000001101110110110100100101011001111010110110101', '110110100010110100000011001010110110111011100011', '011010011010011000101001111111101100100100010011', '110000011001010010001110100001110100011101011110', '011100001000101011010010110111011011001111000000', '001101001111100000100010111100001100011001101101', '100001001011101101000100011100111101110011001100', '000000100111011001010111000010001011010110111111', '011011010101010101100000101011110111110010100101', '110000101100000111101001011010100100101111110011', '100110011100001100010011100101111100100100011111', '001001010001101110001011110001110001011111010000', '001100110011000011000101110110011010001101101101', '000110000001110001011101011101011100011001101101'])
print(a)
a = client_key_receive(a)
print(a)
"""
