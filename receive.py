import os
import argparse
import base64

def decode_exfil_data(data):
    bytes = []
    output = ''
    for url in data:
        bytes.append(url.split('.')[0][5:])
    for b in bytes:
        output += (chr(int(b)))
    return(base64.b64decode(output).decode('utf-8'))



parser = argparse.ArgumentParser(description='Receive exfiltrated data via nginx logs.')

# Argument for file path to nginx log
parser.add_argument('--file', help='Your log file storing the encoded results')

args = parser.parse_args()

# Nginx log file path
file_path = args.file

log_file = open(file_path, 'r')

logs = []
urls = []

if(log_file != None):
    for log in log_file:
        logs.append(log)

for log in logs:
    url = log.split(' ')[10]
    print(url)
    if("lotech" in url):
        urls.append(url)

for url in urls:
    print(url)

#print(decode_exfil_data(urls))
