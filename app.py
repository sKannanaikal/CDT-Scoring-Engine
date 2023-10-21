from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template, request
import atexit
import cv2
import time
import os
import signal
import subprocess

app = Flask(__name__)

flagContentbox1 = '' #update for all boxes
flagLocationbox1 = '' #update for all boxes
flagContentbox2 = '' #update for all boxes
flagLocationbox2 = '' #update for all boxes
flagContentbox3 = '' #update for all boxes
flagLocationbox3 = '' #update for all boxes
flagContentbox4 = '' #update for all boxes
flagLocationbox4 = '' #update for all boxes
flagContentbox5 = '' #update for all boxes
flagLocationbox5 = '' #update for all boxes
flagContentbox6 = '' #update for all boxes
flagLocationbox6 = '' #update for all boxes
flagContentbox7 = '' #update for all boxes
flagLocationbox7 = '' #update for all boxes
flagContentbox8 = '' #update for all boxes
flagLocationbox8 = '' #update for all boxes

box1Owned = False
box2Owned = False
box3Owned = False
box4Owned = False
box5Owned = False
box6Owned = False
box7Owned = False
box8Owned = False

redTeamScore = 0
blueTeamScore = 0

blueColorHexCode = '#003cff'
redColorHexCode = '#ff0800'    

roundCount = 0


@app.route("/", methods = ['GET'])
def homePage():
    return render_template("index.html", redTeamScore=redTeamScore, blueTeamScore=blueTeamScore, redTeamColor=redColorHexCode, blueTeamColor=blueColorHexCode, 
                           roundCount=roundCount, box1Owned=box1Owned, box2Owned=box2Owned, box3Owned=box3Owned, box4Owned=box4Owned,
                           box5Owned=box5Owned, box6Owned=box6Owned, box7Owned=box7Owned, box8Owned=box8Owned)
#update this shit
def flagToggleVerification(team, flagContent, flagLocation, box):
    global box1Owned
    global box2Owned
    global box3Owned
    global box4Owned
    global box5Owned
    global box6Owned
    global box7Owned
    global box8Owned

    global flagContentbox1
    global flagLocationbox1
    global flagContentbox2
    global flagLocationbox2
    global flagContentbox3
    global flagLocationbox3
    global flagContentbox4
    global flagLocationbox4
    global flagContentbox5
    global flagLocationbox5
    global flagContentbox6
    global flagLocationbox6
    global flagContentbox7
    global flagLocationbox7
    global flagContentbox8
    global flagLocationbox8

    #there might be an issue here with local variabliization of the parametrs probably will not be referring to the same parameter
    if team == 'red' and flagContent == '' and flagLocation == '':
            flagContent = request.form['flag']
            flagLocation = request.form['location']
            print(f'[+] Red Team Succesfully Added a Flag onto {box}') # update the name of the boxes
            print(f'{flagContent} at {flagLocation}')
            if box == 'box1':
                box1Owned = True
            elif box == 'box2':
                box2Owned = True
            elif box == 'box3':
                box3Owned = True
            elif box == 'box4':
                box4Owned = True
            elif box == 'box5':
                box5Owned = True
            elif box == 'box6':
                box6Owned = True
            elif box == 'box7':
                box7Owned = True
            elif box == 'box8':
                box8Owned = True
            return f'[+] Red Team Succesfully Added a Flag onto {box}'
    elif team == 'blue' and flagContent != '' and flagLocation != '':
        removalflagContent = request.form['flag']
        removalflagLocation = request.form['location']
        if(removalflagContent == flagContent and removalflagLocation == flagLocation):
            flagContent = ''
            flagLocation = ''
            print(f'[+] Blue Team Succesfully Removed a Flag from {box}') # update the name of the boxes
            if box == 'box1':
                box1Owned = False
            elif box == 'box2':
                box2Owned = False
            elif box == 'box3':
                box3Owned = False
            elif box == 'box4':
                box4Owned = False
            elif box == 'box5':
                box5Owned = False
            elif box == 'box6':
                box6Owned = False
            elif box == 'box7':
                box7Owned = False
            elif box == 'box8':
                box8Owned = False
            return f'[+] Blue Team Succesfully Removed a Flag from {box}'
        else:
            return '[-] Thats not the right flag try again'
    elif team == 'red' and flagLocation != '' and flagContent != '':
        return f'[-] Flag already exists on {box} somewhere else.  Insertion of Flag Denied!'
    elif team == 'blue' and flagContent == '' and flagLocation == '':
        return f'[-] Flag does not exist on the {box}.  Removal of Flag Denied!'

@app.route("/flag", methods = ['POST'])
def box1Toggle():
    global box1Owned
    global box2Owned
    global box3Owned
    global box4Owned
    global box5Owned
    global box6Owned
    global box7Owned
    global box8Owned

    global flagContentbox1
    global flagLocationbox1
    global flagContentbox2
    global flagLocationbox2
    global flagContentbox3
    global flagLocationbox3
    global flagContentbox4
    global flagLocationbox4
    global flagContentbox5
    global flagLocationbox5
    global flagContentbox6
    global flagLocationbox6
    global flagContentbox7
    global flagLocationbox7
    global flagContentbox8
    global flagLocationbox8

    if request.method == 'POST':
        team = request.form['team']
        box = request.form['hostname']
        flagContent = request.form['flag']
        flagLocation = request.form['location']
        if box == 'box1':
            if team == 'blue':
                if flagContentbox1 != '' and flagLocationbox1 != '':
                    if flagContent == flagContentbox1 and flagLocation == flagLocationbox1:
                        flagContentbox1 = ''
                        flagLocationbox1 = ''
                        box1Owned = False
                        print('[+] Blue Team Removed Flag on machine')
                        return '[+] Blue Team Removed Flag on machine'
                    else:
                        return '[+] Try again seems like that was not correct'
            elif team == 'red':
                if flagContentbox1 != '' and flagLocationbox1 != '':
                    return '[+] Flag Already Exists on Machine'
                else:
                    flagContentbox1 = flagContent
                    flagLocationbox1 = flagLocation
                    box1Owned = True
                    print(f'[+] Red team succesfully uploaded flag onto machine')
                    return f'[+] Red team succesfully uploaded flag onto machine'
        elif box == 'box2':
            if team == 'blue':
                if flagContentbox2 != '' and flagLocationbox2 != '':
                    if flagContent == flagContentbox2 and flagLocation == flagLocationbox2:
                        flagContentbox2 = ''
                        flagLocationbox2 = ''
                        box2Owned = False
                        print('[+] Blue Team Removed Flag on machine')
                        return '[+] Blue Team Removed Flag on machine'
                    else:
                        return '[+] Try again seems like that was not correct'
            elif team == 'red':
                if flagContentbox2 != '' and flagLocationbox2 != '':
                    return '[+] Flag Already Exists on Machine'
                else:
                    flagContentbox2 = flagContent
                    flagLocationbox2 = flagLocation
                    box2Owned = True
                    print(f'[+] Red team succesfully uploaded flag onto machine')
                    return f'[+] Red team succesfully uploaded flag onto machine'
        elif box == 'box3':
            if team == 'blue':
                if flagContentbox3 != '' and flagLocationbox3 != '':
                    if flagContent == flagContentbox3 and flagLocation == flagLocationbox3:
                        flagContentbox3 = ''
                        flagLocationbox3 = ''
                        box3Owned = False
                        print('[+] Blue Team Removed Flag on machine')
                        return '[+] Blue Team Removed Flag on machine'
                    else:
                        return '[+] Try again seems like that was not correct'
            elif team == 'red':
                if flagContentbox3 != '' and flagLocationbox3 != '':
                    return '[+] Flag Already Exists on Machine'
                else:
                    flagContentbox3 = flagContent
                    flagLocationbox3 = flagLocation
                    box3Owned = True
                    print(f'[+] Red team succesfully uploaded flag onto machine')
                    return f'[+] Red team succesfully uploaded flag onto machine'
        elif box == 'box4':
            if team == 'blue':
                if flagContentbox4 != '' and flagLocationbox4 != '':
                    if flagContent == flagContentbox4 and flagLocation == flagLocationbox4:
                        flagContentbox4 = ''
                        flagLocationbox4 = ''
                        box4Owned = False
                        print('[+] Blue Team Removed Flag on machine')
                        return '[+] Blue Team Removed Flag on machine'
                    else:
                        return '[+] Try again seems like that was not correct'
            elif team == 'red':
                if flagContentbox4 != '' and flagLocationbox4 != '':
                    return '[+] Flag Already Exists on Machine'
                else:
                    flagContentbox4 = flagContent
                    flagLocationbox4 = flagLocation
                    box4Owned = True
                    print(f'[+] Red team succesfully uploaded flag onto machine')
                    return f'[+] Red team succesfully uploaded flag onto machine'
        elif box == 'box5':
            if team == 'blue':
                if flagContentbox5 != '' and flagLocationbox5 != '':
                    if flagContent == flagContentbox5 and flagLocation == flagLocationbox5:
                        flagContentbox5 = ''
                        flagLocationbox5 = ''
                        box5Owned = False
                        print('[+] Blue Team Removed Flag on machine')
                        return '[+] Blue Team Removed Flag on machine'
                    else:
                        return '[+] Try again seems like that was not correct'
            elif team == 'red':
                if flagContentbox5 != '' and flagLocationbox5 != '':
                    return '[+] Flag Already Exists on Machine'
                else:
                    flagContentbox5 = flagContent
                    flagLocationbox5 = flagLocation
                    box5Owned = True
                    print(f'[+] Red team succesfully uploaded flag onto machine')
                    return f'[+] Red team succesfully uploaded flag onto machine'
        elif box == 'box6':
            if team == 'blue':
                if flagContentbox6 != '' and flagLocationbox6 != '':
                    if flagContent == flagContentbox6 and flagLocation == flagLocationbox6:
                        flagContentbox6 = ''
                        flagLocationbox6 = ''
                        box6Owned = False
                        print('[+] Blue Team Removed Flag on machine')
                        return '[+] Blue Team Removed Flag on machine'
                    else:
                        return '[+] Try again seems like that was not correct'
            elif team == 'red':
                if flagContentbox6 != '' and flagLocationbox6 != '':
                    return '[+] Flag Already Exists on Machine'
                else:
                    flagContentbox6 = flagContent
                    flagLocationbox6 = flagLocation
                    box6Owned = True
                    print(f'[+] Red team succesfully uploaded flag onto machine')
                    return f'[+] Red team succesfully uploaded flag onto machine'
        elif box == 'box7':
            if team == 'blue':
                if flagContentbox7 != '' and flagLocationbox7 != '':
                    if flagContent == flagContentbox7 and flagLocation == flagLocationbox7:
                        flagContentbox7 = ''
                        flagLocationbox7 = ''
                        box7Owned = False
                        print('[+] Blue Team Removed Flag on machine')
                        return '[+] Blue Team Removed Flag on machine'
                    else:
                        return '[+] Try again seems like that was not correct'
            elif team == 'red':
                if flagContentbox7 != '' and flagLocationbox7 != '':
                    return '[+] Flag Already Exists on Machine'
                else:
                    flagContentbox7 = flagContent
                    flagLocationbox7 = flagLocation
                    box7Owned = True
                    print(f'[+] Red team succesfully uploaded flag onto machine')
                    return f'[+] Red team succesfully uploaded flag onto machine'
        elif box == 'box8':
            if team == 'blue':
                if flagContentbox8 != '' and flagLocationbox8 != '':
                    if flagContent == flagContentbox8 and flagLocation == flagLocationbox8:
                        flagContentbox8 = ''
                        flagLocationbox8 = ''
                        box8Owned = False
                        print('[+] Blue Team Removed Flag on machine')
                        return '[+] Blue Team Removed Flag on machine'
                    else:
                        return '[+] Try again seems like that was not correct'
            elif team == 'red':
                if flagContentbox8 != '' and flagLocationbox8 != '':
                    return '[+] Flag Already Exists on Machine'
                else:
                    flagContentbox8 = flagContent
                    flagLocationbox8 = flagLocation
                    box8Owned = True
                    print(f'[+] Red team succesfully uploaded flag onto machine')  
                    return f'[+] Red team succesfully uploaded flag onto machine'        

def pointsUpdated():
    global redTeamScore
    global blueTeamScore
    global roundCount

    global box1Owned
    global box2Owned
    global box3Owned
    global box4Owned
    global box5Owned
    global box6Owned
    global box7Owned
    global box8Owned

    if(box1Owned):
        redTeamScore += 1
    else:
        blueTeamScore += 1

    if(box2Owned):
        redTeamScore += 1
    else:
        blueTeamScore += 1

    if(box3Owned):
        redTeamScore += 1
    else:
        blueTeamScore += 1

    if(box4Owned):
        redTeamScore += 1
    else:
        blueTeamScore += 1

    if(box5Owned):
        redTeamScore += 1
    else:
        blueTeamScore += 1

    if(box6Owned):
        redTeamScore += 1
    else:
        blueTeamScore += 1

    if(box7Owned):
        redTeamScore += 1
    else:
        blueTeamScore += 1

    if(box8Owned):
        redTeamScore += 5
    else:
        blueTeamScore += 5

    roundCount += 1
    print(f'[+] Points Updated for round: {roundCount - 1} {redTeamScore} {blueTeamScore}')

if __name__ == '__main__':
    pointsUpdater = BackgroundScheduler()
    pointsUpdater.add_job(func=pointsUpdated, trigger="interval", seconds=60)
    pointsUpdater.start()
    app.run(host='0.0.0.0', port=80)
    atexit.register(lambda: pointsUpdater.shutdown())
