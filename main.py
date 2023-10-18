# Rules
# I provide test cases for your code, but if your code fulfills
# the test cases that does not guarantee the function's correctness.
# Test cases are intended to aid in understanding and development.
# If you believe there are errors in the test cases, please inform me.
#
# The assignment is to build non-secure encryption schemes.
# For grade 2: only functionality (completion of at least the first two tasks).
# For grade 5: you must have well-commented and formatted code.
#
# You not allowed to use external libraries.
# You can use the solution codes from the canvas,
# but copy paste all of the code that you used and refere,
# where you copeid from.
# If I find similarity without reference, both of the exam will be graded to 0 points.
#
# Below, you'll find the skeleton of the exam.
# Complete the function bodies and submit this file.
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

# ----------------------------
# # Task 1
# Create an encryption function that XORs each input byte with a changing key.
# We have a one byte sized key and encrypt the first byte of the plain message with that key.
# Power the key byte to 2, add 136 and modulo by 256.
# (e.g. if the key is 2 then the second byte will be encrypted by 155)
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

# ----------------------------
# Task 2:
# Extend the previous scheme with the following:
# When the key is 0 or 1, use the previous plain message byte as the encryption key.
# Hint: In the decryption algorithm, you receive the cipher as input.
# To determine the decryption mode of the algorithm, you need to use the decrypted value
# of the previous byte when you encounter 0 or 1.
'''refer: https://github.com/mileyDu123/Python_security_course/blob/main/10.12.ipynb'''
def encrypt_with_power2(plaintext, key, mode):
    '''
    >>> string2hex(encrypt_with_power2('Hello',33,'encrypt'))
    '69ac3515d6'
    >>> string2hex(encrypt_with_power2(hex2string('acc5522cca'),11,'encrypt'))
    'a7694ae402'
    >>> string2hex(encrypt_with_power2(hex2string('123456aaab'),11,'encrypt'))
    '19269ab263'
    >>> string2hex(encrypt_with_power2(hex2string('abcc156622'),11,'encrypt'))
    'a067d46ffb'
    >>> string2hex(encrypt_with_power2(hex2string('8765432145'),11,'encrypt'))
    '8ce2fa187c'
    >>> string2hex(encrypt_with_power2(hex2string('123456aaab'),139,'encrypt'))
    '99269ab263'
    >>> string2hex(encrypt_with_power2(hex2string('abcc156622'),139,'encrypt'))
    '2067d46ffb'
    >>> string2hex(encrypt_with_power2(hex2string('8765432145'),139,'encrypt'))
    '0ce2fa187c'
    >>> encrypt_with_power2(encrypt_with_power2('Hello',11,'encrypt'),11,'decrypt')
    'Hello'
    >>> encrypt_with_power2(encrypt_with_power2('Cryptography',11,'encrypt'),11,'decrypt')
    'Cryptography'
    >>> encrypt_with_power2(encrypt_with_power2('Hello',123,'encrypt'),123,'decrypt')
    'Hello'
    >>> encrypt_with_power2(encrypt_with_power2('Cryptography',10,'encrypt'),10,'decrypt')
    'Cryptography'
    '''
    str = plaintext
    bin_key = bin(key)[2:]
    result = ""

    for i in range(0, len(str)):
        print(str)
        print(str[0])
        bin_num = bin(ord(str[0]))[2:]
        while len(bin_key) < len(bin_num):
            bin_key = "0" + bin_key
        while len(bin_key) > len(bin_num):
            bin_num = "0" + bin_num

        cipher = ""
        for j in range(len(bin_num)):
            cipher = cipher + bin(int(bin_num[j]) ^ int(bin_key[j]))[2:]
        real_key = int(cipher, base=2)
        print("real key of the first byte:", real_key)

        result = result + chr(real_key)
        str = str[1:]
        if mode == "encrypt" and (key == 1 or key == 0):
            bin_key = bin(real_key)[2:]
        elif mode == "decrypt" and (key == 1 or key == 0):
            bin_key = bin_num

    return result


# ----------------------------
# # Task 3.
# Create a function that swaps the first 4 bit with the second 4 bit in a byte.
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

# ----------------------------
# # Task 4.
# Extend the previous scheme with the following:
# In every step use the swap_lower_and_upper_bits to obfuscate the keys
def encrypt_with_power3(plaintext, key, mode):
    '''
    >>> string2hex(encrypt_with_power3('Hello',33,'encrypt'))
    '69f9e5f172'
    >>> string2hex(encrypt_with_power3(hex2string('acc5522cca'),11,'encrypt'))
    'a70f9ce843'
    >>> string2hex(encrypt_with_power3(hex2string('123456aaab'),11,'encrypt'))
    '1915ca2336'
    >>> string2hex(encrypt_with_power3(hex2string('abcc156622'),11,'encrypt'))
    'a076dfa8e6'
    >>> string2hex(encrypt_with_power3(hex2string('a076dfa8e6'),11,'decrypt'))
    'abcc156622'
    >>> string2hex(encrypt_with_power3(hex2string('8765432145'),11,'encrypt'))
    '8c1dcfa0dd'
    >>> string2hex(encrypt_with_power3(hex2string('a076dfa8e6'),139,'decrypt'))
    '2bc41b217b'
    >>> string2hex(encrypt_with_power3(hex2string('8765432145'),139,'encrypt'))
    '0c1dcfa0dd'
    >>> encrypt_with_power3(encrypt_with_power3('Hello',11,'encrypt'),11,'decrypt')
    'Hello'
    >>> encrypt_with_power3(encrypt_with_power3('Cryptography',11,'encrypt'),11,'decrypt')
    'Cryptography'
    '''
    return ''

# ----------------------------
# Task 5:
# Create a new scheme that uses the previous scheme as a substep.
# This encryption algorithm is working with 8-byte length keys.
# For the 1,9,17...th bytes, use the previous encryption with the first byte of the key list as key.
# For the 2,10,18...th bytes, use the previous encryption with the second byte of the key list as key, etc.
# Repeat this process for all 8 bytes in the key list.
# That means this algorithm splits up the input to 8 new inputs and feeds those 8 inputs for the previous scheme
# that uses only one byte length key.
def encrypt_with_power3_8byte(plaintext, key, mode):
    '''
    >>> key1 = [139,2,11,4,5,6,7,11]
    >>> key2 = [139,76,11,98,33,99,11,234]
    >>> string2hex(encrypt_with_power3_8byte('Hello',key1,'encrypt'))
    'c36767686a'
    >>> string2hex(encrypt_with_power3_8byte(hex2string('acc5522cca'),key1,'encrypt'))
    '27c75928cf'
    >>> string2hex(encrypt_with_power3_8byte(hex2string('acc5522cca'),key2,'encrypt'))
    '2789594eeb'
    >>> string2hex(encrypt_with_power3_8byte(hex2string('1234123123'),key2,'encrypt'))
    '9978195302'
    >>> string2hex(encrypt_with_power3_8byte(hex2string('5646234325'),key2,'encrypt'))
    'dd0a282104'
    >>> string2hex(encrypt_with_power3_8byte('I love Cryptography!!!',key1,'encrypt'))
    'c222676b73632748e6b1b6fd75ade955f1e4b3bce3ef'
    >>> string2hex(encrypt_with_power3_8byte("To be, or not to be, that is the question: Whether 'tis nobler in the mind to suffer",key1,'encrypt'))
    'df6d2b66602a276437e86ce66eeaef9932eeadb1e2ba7eafb8a1e56ee8b0aea1a1e9f478fffda3e6f6b6b84ae9f8baf5e9f3ac3aec74b73deff7e371e96fa974f6acec75e43df074e2e5ac69f73d6e68e7fee46f'
    >>> string2hex(encrypt_with_power3_8byte('Hello world, now I can encpryt with longer key!!',key1,'encrypt'))
    'c36767686a267064f6a4a2a53aa4f481a9c5eafea3a036abf3e2be6fb1b0e6b374ecac3de0e6a4ee78fea976e4e4efbc'
    >>> encrypt_with_power3_8byte(hex2string('c36767686a267064f6a4a2a53aa4f481a9c5eafea3a036abf3e2be6fb1b0e6b374ecac3de0e6a4ee78fea976e4e4efbc'),key1,'decrypt')
    'Hello world, now I can encpryt with longer key!!'
    >>> string2hex(encrypt_with_power3_8byte('Our goal is to test out if our algorithm working well with splitting the input.',key1,'encrypt'))
    'c477792462696667d4a154a96ea5bbb2e4ffe3bdadbb62eaf1e7b972bdb6e6afe0fff06fe5fda2a9a1fbfb6feaf4a0eeb8f6e471f43db3f4f8f0b86efc71e069f5e5e27aa169f578b8e8ef6ded6933'
    >>> encrypt_with_power3_8byte(encrypt_with_power3_8byte('Hello',key1,'encrypt'),key1,'decrypt')
    'Hello'
    >>> encrypt_with_power3_8byte(encrypt_with_power3_8byte('Hello',key2,'encrypt'),key2,'decrypt')
    'Hello'
    >>> encrypt_with_power3_8byte(encrypt_with_power3_8byte('Hello',key1,'encrypt'),key1,'decrypt')
    'Hello'
    >>> string2hex(encrypt_with_power3_8byte(encrypt_with_power3_8byte('Hello',key1,'encrypt'),key2,'decrypt'))
    '482b6c0a4b'
    >>> encrypt_with_power3_8byte(encrypt_with_power3_8byte('Cryptography',key1,'encrypt'),key1,'decrypt')
    'Cryptography'
    >>> encrypt_with_power3_8byte(encrypt_with_power3_8byte("To be, or not to be, that is the question: Whether 'tis nobler in the mind to suffer",key1,'encrypt'),key1,'decrypt')
    "To be, or not to be, that is the question: Whether 'tis nobler in the mind to suffer"
    >>> encrypt_with_power3_8byte(encrypt_with_power3_8byte('Hello world, now I can encpryt with longer key!!',key1,'encrypt'),key1,'decrypt')
    'Hello world, now I can encpryt with longer key!!'
    >>> encrypt_with_power3_8byte(encrypt_with_power3_8byte('Our goal is to test out if our algorithm working well with joining the chunks.',key1,'encrypt'),key1,'decrypt')
    'Our goal is to test out if our algorithm working well with joining the chunks.'
    '''
    return ''



# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()




