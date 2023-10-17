'''
task1

one-byte key
encrypt all of the bytes of the plain text by adding the key for every one byte and MODULO by 256
'''


def encrypt_by_add_mod(str, key):
    dec_num = [ord(str[i]) for i in range(len(str))]

    result = ""
    for i in range(len(dec_num)):
        result = result + chr((dec_num[i] + key) % 256)

    return result


# print(encrypt_by_add_mod("Hello", 123))
# print(encrypt_by_add_mod(encrypt_by_add_mod("Hello", 123), 133))
# print(encrypt_by_add_mod(encrypt_by_add_mod("Cryptography", 10), 246))


'''
task2

one-byte sized key
XOR the first byte of the plaintext and that will be the cipher for the byte.
encrypt the second  byte use the cipher of the message first byte as key and so on
'''


def encrypt_xor_with_changing_key_by_prev_cipher(text, key, act):
    str = text
    bin_key = bin(key)[2:]
    result = ""

    for i in range(0, len(str)):
        # print(str)
        # print(str[0])
        bin_num = bin(ord(str[0]))[2:]
        while len(bin_key) < len(bin_num):
            bin_key = "0" + bin_key
        while len(bin_key) > len(bin_num):
            bin_num = "0" + bin_num

        # print(bin_num)
        # print(bin_key)

        cipher = ""
        for j in range(len(bin_num)):
            cipher = cipher + bin(int(bin_num[j]) ^ int(bin_key[j]))[2:]
        real_key = int(cipher, base=2)
        # print("real key of the first byte:", real_key)

        result = result + chr(real_key)
        str = str[1:]
        if act == "encrypt":
            bin_key = bin(real_key)[2:]
        elif act == "decrypt":
            bin_key = bin_num
        else:
            break
            return "please choose an action about the text."
        # print(result)
        # print(i, "\n")
    return result


# print(encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt'))
# print(decrypt("3V:V9",123,"decrypt"))
# print(encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt'),123,'decrypt'))
# print(encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Cryptography',10,'encrypt'),10,'decrypt'))



"""
test3

use 4 byte length
key_list = [0x20, 0x44, 0x54,0x20]
"""
key_list = [0x20, 0x44, 0x54, 0x20]
def cipher_calculate(bin_num, bin_key):
    cipher = ""
    for j in range(len(bin_num)):
        cipher = cipher + bin(int(bin_num[j]) ^ int(bin_key[j]))[2:]
    real_key = int(cipher, base=2)

    # print("real key of the first byte:", real_key)
    return real_key

def encrypt_xor_with_changing_key_by_prev_cipher_longer_key(text, keys, act):
    str = text
    result = ""

    bin_key1 = bin(keys[0])[2:]
    bin_key2 = bin(keys[1])[2:]
    bin_key3 = bin(keys[2])[2:]
    bin_key4 = bin(keys[3])[2:]
    bin_key = ""
    for i in range(len(str)):
        # print(str[i+1])
        bin_num = bin(ord(str[i]))[2:]
        # print("element:", str[i], " ", bin_num)
        if i < 4:
            if i == 0:
                bin_key = bin_key1
            elif i == 1:
                bin_key = bin_key2
            elif i == 2:
                bin_key = bin_key3
            elif i == 3:
                bin_key = bin_key4
        elif i >= 4 and act == "encrypt":
            bin_key = bin(ord(result[i - 4]))[2:]
        elif i >= 4 and act == "decrypt":
            bin_key = bin(ord(str[i - 4]))[2:]

        while len(bin_key) < len(bin_num):
            bin_key = "0" + bin_key
        while len(bin_key) > len(bin_num):
            bin_num = "0" + bin_num

        # print("key:", bin_key)

        real_key = cipher_calculate(bin_num, bin_key)

        result = result + chr(real_key)
        # print(chr(real_key), " ", i, "\n")

    return result


# print(encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg', key_list, 'encrypt'))
# print(encrypt_xor_with_changing_key_by_prev_cipher_longer_key('aaabbbb', key_list, 'encrypt'))
# print(encrypt_xor_with_changing_key_by_prev_cipher_longer_key(encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg', key_list, 'encrypt'), key_list, 'decrypt'))
# print(encrypt_xor_with_changing_key_by_prev_cipher_longer_key(encrypt_xor_with_changing_key_by_prev_cipher_longer_key('Hellobello, it will work for a long message as well',key_list, 'encrypt'), key_list, 'decrypt'))