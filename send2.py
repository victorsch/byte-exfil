import requests, base64
from random import randrange
import struct

def encode(message):
    testx = base64.b64encode(message.encode('utf-8'))
    return testx

def to_binary(thestring):
    res = ''.join(format(ord(i), '08b') for i in thestring)
    return res

def start_exfil(binary_data):
    urls = []
    for c in binary_data:
        if c == '0':
            number = randrange(0, 101, 2)  + 1
            urls.append("level" + str(number) + ".lotech.com")
        if c == '1':
            number = randrange(0, 101, 2)
            urls.append("level" + str(number) + ".lotech.com")
    return urls

def start_exfil2(binary_data):
    urls = []
    for c in binary_data:
        num_value = str(c)
        urls.append("level" + str(num_value) + ".lotech.com")
    return(urls)

def decode_exfil_data(data):
    bytes = []
    output = ''
    for url in data:
        bytes.append(url.split('.')[0][5:])
    for b in bytes:
        output += (chr(int(b)))
    return(base64.b64decode(output).decode('utf-8'))


if __name__ == '__main__':
    cipher = encode("poopy butt")
    ex = start_exfil2(cipher)
    out = decode_exfil_data(ex)
    print(out)


