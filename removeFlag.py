import requests
import socket
import os

def main():
    hostname = socket.gethostname()
    filename = input('Enter the full file path : ')
    result = os.path.exists(filename)
    if not result:
        print('[+] File Does not exist try again')
        quit()
    flag = ''
    with open(f'{filename}', 'r') as flagFile:
        flag = flagFile.read()
    
    scoringServer = f'http://192.168.100.10:80/flag' 

    data  = {'flag': f'{flag}','location': f'{filename}','team': 'blue', 'hostname': {hostname}}

    request = requests.post(scoringServer, data=data)
    print(request.text)
main()
