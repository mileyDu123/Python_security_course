"""
homework5
用动态密钥加密文本
其中涉及到
1.异或算法xor a^b
2.取模算法 a%b
3.几个常用ASKII转换函数
--ord()文本转十进制数
--chr()十进制数转文本
4.增加了需要根据变量值判断加密或解密操作的内容，需要增加if判断。其中涉及到xor的部分需要根据文本情况判断
--异或规则：a^b = c then c^b = a, a^c = b
5.在老师给的解决方案里有涉及到的：
--文本切片：chunks = [plaintext[i::key_len] for i in range(key_len)] 切片部分: str[开始: 结尾: 步长]
--可以分几个函数写然后调用
"""

def encrypt_by_add_mod(message, key):
    '''
    >>> encrypt_by_add_mod("Hello",123)
    'Ãàççê'
    >>> encrypt_by_add_mod(encrypt_by_add_mod("Hello",123),133)
    'Hello'
    >>> encrypt_by_add_mod(encrypt_by_add_mod('Cryptography',10),246)
    'Cryptography'
    '''

    ret = ""
    for m in message:
        new_byte_value = (ord(m) + key) % 256
        ret += chr(new_byte_value)
    return ret


def encrypt_xor_with_changing_key_by_prev_cipher(message,key,mode):
    '''
    >>> encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt')
    '3V:V9'
    >>> encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Hello',123,'encrypt'),123,'decrypt')
    'Hello'
    >>> encrypt_xor_with_changing_key_by_prev_cipher(encrypt_xor_with_changing_key_by_prev_cipher('Cryptography',10,'encrypt'),10,'decrypt')
    'Cryptography'
    '''

    ret = ""
    actual_key = key

    for m in message:
        # 同样是十进制异或的问题
        new_byte_value = ord(m) ^ actual_key
        if mode == "encrypt":
            actual_key = new_byte_value
        elif mode == "decrypt":
            actual_key = ord(m)
        else:
            raise Exception(f'Unknown mode {mode}')

        ret += chr(new_byte_value)

    return ret



# key_list = [0x20, 0x44, 0x54, 0x20]
def encrypt_xor_with_changing_key_by_prev_cipher_longer_key(text, keys, act):
    '''
        >>> key_list = [0x20, 0x44, 0x54,0x20]
        >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg', key_list, 'encrypt')
        'A&7D$@P'
        >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key('aaabbbb', key_list, 'encrypt')
        'A%5B#GW'
        >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key(
        ...    encrypt_xor_with_changing_key_by_prev_cipher_longer_key('abcdefg',key_list,'encrypt'),
        ...        key_list,'decrypt')
        'abcdefg'
        >>> encrypt_xor_with_changing_key_by_prev_cipher_longer_key(
        ...    encrypt_xor_with_changing_key_by_prev_cipher_longer_key('Hellobello, it will work for a long message as well',key_list,'encrypt'),
        ...        key_list,'decrypt')
        'Hellobello, it will work for a long message as well'
        '''

    str = text
    result = ""

    bin_key = ""
    for i in range(len(str)):
        # bin_num = bin(ord(str[i]))[2:]
        '''把二进制异或改成十进制异或会简化一点'''
        num = ord(str[i])
        # bin_keys = [bin(keys[k])[2:] for k in range(len(keys))]
        if i < 4:
            # bin_key = bin_keys[i]
            key = keys[i]
        elif i >= 4 and act == "encrypt":
            # bin_key = bin(ord(result[i - 4]))[2:]
            key = ord(result[i-4])
        elif i >= 4 and act == "decrypt":
            # bin_key = bin(ord(str[i - 4]))[2:]
            key = ord(str[i-4])

        cipher = 0
        cipher += num ^ key # 十进制异或
        real_key = cipher

        result = result + chr(real_key)

    '''
    key_len = len(key)
    chunks = [plaintext[i::key_len] for i in range(key_len)]
    chunks_cipher = []
    for i in range(key_len):
        cipher = encrypt_xor_with_changing_key_by_prev_cipher(chunks[i], key[i], mode)
        chunks_cipher.append(cipher)

    ret = ''
    for i in range(len(plaintext)):
        which_chunk = i % len(chunks_cipher)
        character_num = i // len(chunks_cipher)
        ret += chunks_cipher[which_chunk][character_num]

    return ret
    '''

    return result

'''
homework4
从加密文本找出密钥 并返回解密文本
前提：已知使用异或加密，且是重复 单字节密钥 暴力破解设置一个单字节字符的最大值，256
'''

'''
hex2bin 十六进制转二进制 bin(int(hex_number_string, base = 16))[2:] (因为十六进制有个2位前缀)
bin2hex 二进制转十六进制 hex(int(bin_number_string, base = 2))[2:] (二进制也有个2位前缀)
hex2string 十六进制转字符串 chr(int(hex_number_string, base = 16))
string2hex 字符串转十六进制 hex(ord(string_element))[2:].rjust(width:2,fillchar:'0')

hex_xor 用十六进制xor运算（转换成二进制或十进制进行异或，一般十进制比较简洁，但目前可能比较习惯二进制，需要对齐补零）
对齐补零，一般是字符串补零，str + "0" 或 "0" + str 就行

一般chr 和 ord 都是ASKII码的函数，如果需要转base64之类的编码需要单独给出
base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
参见9.27作业
'''
def hex2string(hex_message):
    ret = ""
    for i in range(0,len(hex_message),2):
        ret += chr(int(hex_message[i:i+2],16)) # 直接用内置函数chr()就可以
    return ret

def string2hex(message):
    ret = ""
    for c in message:
        ret += hex(ord(c))[2:].rjust(2,'0') # 这里用了右对齐.rjust(填充字符后字符串的长度（因为是十六进制数所以定成2），填充的字符) 感觉不用应该也行
    return ret

def decrypt_single_byte_xor(cipher):

    # Run a maximum search on the results
    best = None
    best_count = None
    for key in range(256):
        hex_key = hex(key)[2:].zfill(2)
        decrypted_message = hex2string(encrypt_single_byte_xor(cipher,hex_key))
        # print(decrypted_message)
        # We count how many normal characters can be found in a message
        # Results that decrypted message that has the most normal character
        # You can use more sophisticated function to determine is a text normal text or not like character distribution for example.
        actual_count = count_simple_text_chars(decrypted_message)
        if best == None or best_count < actual_count:
            best = decrypted_message
            best_count = actual_count

    return best

'''
自己写的

'''

valid_characters = "abcdefg hijklmn opqrst uvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ!?"

def decrypt_single_byte_xor(hex_string):
    # 1.hex2dec
    s1 = bin(int(hex_string, 16))[2:]
    while len(s1) % 8 != 0:
        s1 = "0" + s1
    # print("s1:",s1,"\nlength:",len(s1))

    num = 0
    while num <= 255:
        # print(num)
        # 2.find key
        key1 = bin(num)[2:]
        key2 = key1
        while len(key2) < len(s1):
            # print(i)
            key2 = key2 + key1
            # i += 1
        # print("key:",key2,"\nlength:",len(key2))

        # 3.do xor calculate and find the decrypted text
        dcp_s2 = ""
        for i in range(0, len(s1), 1):
            dcp_s2 = dcp_s2 + bin(int(s1[i]) ^ int(key2[i]))[2:]
        # print("dcp_s2:",dcp_s2,"\n")

        # bin2string
        text_string = ""
        for i in range(0, len(dcp_s2), 8):
            chunk = dcp_s2[i: i + 8]
            dec_num = int(chunk, 2)
            text_string = text_string + chr(dec_num)
        result = text_string
        # print(result)

        if all(char in valid_characters for char in result):
            return result
            break
        else:
            num += 1


# print(decrypt_single_byte_xor("c2cfc6c6c5"))
# print(decrypt_single_byte_xor("e9c88081f8ced481c9c0d7c481c7ced4cfc581ccc480"))
# print(decrypt_single_byte_xor("b29e9f96839085849d9085989e9f82d1889e84d199908794d197989f95d1859994d181908282869e8395d0"))
# print(decrypt_single_byte_xor("e1ded996ddd8d9c1c596c1ded7c296dfc596ded7c6c6d3d8dfd8d18996e1ded3c4d396d7db96ff89"))

'''
9.27作业上交版本
'''

def hex2base64(s):
    base64_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binary = bin(int(s, base=16))[2:]
    # print(binary)
    while len(binary) % 8 != 0:
        binary = "0" + binary
    while len(binary) % 6 != 0:
        binary = binary + "0"
    # print(binary+"\n")

    result = ""
    for i in range(0, len(binary), 6):
        new_binary = binary[i:i + 6]
        # print("new:"+new_binary)
        dec_value = int(new_binary, 2)
        # print("dec:",dec_value)
        result += base64_string[dec_value]

    add_padding = len(result) % 4
    if add_padding > 0:
        result += "=" * (4 - add_padding)

    return result

print(hex2base64('61'))

print(hex2base64("123456789abcde"))

'''
9.19作业和9.13作业主要是字符串操作
'''

'''
9.13 输出指定范围值，属于基础操作，不一定会考
'''
def bound_value(value, minimum_value=0, maximum_value=100):

    return max(minimum_value, min(value, maximum_value))


print(bound_value(12))
print(bound_value(-2))
print(bound_value(111))
print(bound_value(0))
print(bound_value(1))
print(bound_value(99))
print(bound_value(199, maximum_value=200))
print(bound_value(199, minimum_value=100))
print(bound_value(-100, minimum_value=100))
print(bound_value(100, minimum_value=100))
print(bound_value(100, 1, 4))
print(bound_value(-1, 2, 4))
print(bound_value(3011, 2, 4))

'''
9.19
The function accepts a list of integers.
Create a new list that converts the passed numbers to characters with the chr function
Join this list of characters to a string
Make the string lower case
Create a string that contains the letters of the string from 2 to 10th character and put it twice after each other.
'''


def test_function(int_l):
    chr_l = [chr(i) for i in int_l]

    s = ''.join(chr_l)

    s1 = s.lower()
    s2 = s1[2:10] * 2

    print(chr_l)
    print(s)
    print(s1)
    print(s2)

    return s2

