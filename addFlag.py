import random
import requests
import socket

def main():
    prefix = ['rt', 'redteam', 'rteam', 'red', 'russia', 'soviets', 'motherRussia', 'motherrussia', 'russians']
    hostname = socket.gethostname()
    filename = input('Enter the full file path to save/name file: ')
    message = input ('Enter the message you would like to embed in flag: ')
    flag = f'{prefix[random.randint(0, len(prefix) - 1)]}' + '{' + f'{message}' + '}'
    
    with open(f'{filename}', 'w+') as flagFile:
        flagFile.write(flag)

    
    scoringServer = f'http://192.168.100.10:80/flag' 

    data  = {'flag': f'{flag}','location': f'{filename}','team': 'red', 'hostname': {hostname}}

    request = requests.post(scoringServer, data=data)
    print(request.text)

if __name__ == '__main__':
    main()
