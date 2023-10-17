import requests
import socket

def main():
    hostname = socket.gethostname()
    filename = input('Enter the full file path to the flag: ')
    flag = ''
    with open(f'{filename}', 'r') as flagFile:
        flag = flagFile.read()

    
    scoringServer = f'http://127.0.0.1:5000/{hostname}' 

    data  = {'flag': f'{flag}','location': f'{filename}','team': 'blue', 'hostname': {hostname}}

    request = requests.post(scoringServer, data=data)
    print(request.text)
main()