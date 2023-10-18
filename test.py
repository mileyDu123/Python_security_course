def string2hex(message):
    ret = ""

    for c in message:
        ret += hex(ord(c))[2:].rjust(2,'0')

    return ret

def hex2string(hex_message):
    ret = ""
    for i in range(0,len(hex_message),2):
        ret += chr(int(hex_message[i:i+2],16))

    return ret
# print(hex2string('acc5522cca'))
'''def encrypt_with_power(plaintext, key):
    result = ""
    hex_num = string2hex(plaintext)
    dec_num = [ord(plaintext[i]) for i in range(len(plaintext))]
    print (dec_num)
    real_key = key
    for i in range(len(dec_num)):
        new_key = dec_num[i] ^ (((real_key * real_key) + 133) % 256)
        print (new_key)
        real_key = new_key
        result = result + chr(new_key)

    dec_num = [ord(plaintext[i]) for i in range(len(plaintext))]
    return result

print(encrypt_with_power(hex2string('acc5522cca'),11))
print(string2hex(encrypt_with_power(hex2string('acc5522cca'),11)))
print(((11 * 11) + 133) % 256)'''

# def swap_lower_and_upper_bits(input):
#
#     bin_num = bin(input)[2:]
#     while len(bin_num)%8 != 0:
#         bin_num = "0" + bin_num
#     print (bin_num)
#     # result = ""
#     result = int((bin_num[-4:] + bin_num[0:4]),2)
#     return result
#
# print (swap_lower_and_upper_bits(2))
def swap_lower_and_upper_bits(input):
    '''
    >>> swap_lower_and_upper_bits(0)
    0
    >>> swap_lower_and_upper_bits(1)
    16
    >>> swap_lower_and_upper_bits(2)
    32
    >>> swap_lower_and_upper_bits(8)
    128
    >>> bin(swap_lower_and_upper_bits(0b1111))
    '0b11110000'
    >>> bin(swap_lower_and_upper_bits(0b10011010))
    '0b10101001'
    '''
    bin_num = bin(input)[2:]
    while len(bin_num) % 8 != 0:
        bin_num = "0" + bin_num
    result = int((bin_num[-4:] + bin_num[0:4]), 2)

    return result

def encrypt_with_power(plaintext, key):
    '''
    >>> string2hex(encrypt_with_power(hex2string('acc5522cca'),11))
    'a7c4dbf5b3'
    >>> string2hex(encrypt_with_power(hex2string('123456aaab'),11))
    '1935df73d2'
    >>> string2hex(encrypt_with_power(hex2string('abcc156622'),11))
    'a0cd9cbf5b'
    >>> string2hex(encrypt_with_power(hex2string('8765432145'),11))
    '8c64caf83c'
    >>> encrypt_with_power(encrypt_with_power('Hello',123),123)
    'Hello'
    >>> encrypt_with_power(encrypt_with_power('Cryptography',10),10)
    'Cryptography'
    '''
    result = ""
    dec_num = [ord(plaintext[i]) for i in range(len(plaintext))]
    real_key = key
    for i in range(len(dec_num)):
        new_key = dec_num[i] ^ (((real_key * real_key) + 133) % 256)
        result = result + chr(new_key)

    return result