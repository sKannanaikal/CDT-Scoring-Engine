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

box1Owned = True
box2Owned = False
box3Owned = False
box4Owned = False
box5Owned = False
box6Owned = False
box7Owned = True
box8Owned = True

timerBegin = False

redTeamScore = 10000
blueTeamScore = 995

blueColorHexCode = '#003cff'
redColorHexCode = '#ff0800'    

videoPlayerProc = None
roundCount = 0

def nukeLaunch():
    global timerBegin
    global videoPlayerProc 

    if(videoPlayerProc == None and timerBegin == True):
        videoPlayerProc = subprocess.Popen(["C:/Program Files/Windows Media Player/wmplayer.exe", 'C:\\Users\\Sean Kannanaikal\\Documents\\CDT Scoring Engine\\ufo.mp4']) #update this to the mp3 file
    ##use a different function and check if the process already exists if its a nonzero value then don't start if it has been removed then change pid to 0 to know you can play again
    if(timerBegin == False and videoPlayerProc != None):
        os.kill(videoPlayerProc.pid, signal.SIGTERM)
        videoPlayerProc = None

def startCountdown():
    if(flagContentbox1 != '' and flagContentbox2 != '' and 
       flagContentbox3 != '' and flagContentbox4 != '' and 
       flagContentbox5 != '' and flagContentbox6 != '' and 
       flagContentbox7 != '' and flagContentbox8 != ''):
        timerBegin = True
    else:
        timerBegin = False

@app.route("/", methods = ['GET'])
def homePage():
    return render_template("index.html", redTeamScore=redTeamScore, blueTeamScore=blueTeamScore, redTeamColor=redColorHexCode, blueTeamColor=blueColorHexCode, 
                           startCountDown=timerBegin, roundCount=roundCount, box1Owned=box1Owned, box2Owned=box2Owned, box3Owned=box3Owned, box4Owned=box4Owned,
                           box5Owned=box5Owned, box6Owned=box6Owned, box7Owned=box7Owned, box8Owned=box8Owned)

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
        if box == 'box1':
            flagToggleVerification(team, flagContentbox1, flagLocationbox1, box)
        elif box == 'box2':
            flagToggleVerification(team, flagContentbox2, flagLocationbox2, box)
        elif box == 'box3':
            flagToggleVerification(team, flagContentbox3, flagLocationbox3, box)
        elif box == 'box4':
            flagToggleVerification(team, flagContentbox4, flagLocationbox4, box)
        elif box == 'box5':
            flagToggleVerification(team, flagContentbox5, flagLocationbox5, box)
        elif box == 'box6':
            flagToggleVerification(team, flagContentbox6, flagLocationbox6, box)
        elif box == 'box7':
            flagToggleVerification(team, flagContentbox7, flagLocationbox7, box)
        elif box == 'box8':
            flagToggleVerification(team, flagContentbox8, flagLocationbox8, box)            

def pointsUpdated():
    global redTeamScore
    global blueTeamScore
    global roundCount

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
    countDownChecker = BackgroundScheduler()
    nukeLauncher = BackgroundScheduler()

    pointsUpdater.add_job(func=pointsUpdated, trigger="interval", seconds=60)
    countDownChecker.add_job(func=startCountdown, trigger="interval", seconds=3)
    nukeLauncher.add_job(func=nukeLaunch, trigger="interval", seconds=5)

    pointsUpdater.start()
    countDownChecker.start()
    nukeLauncher.start()

    app.run()
    atexit.register(lambda: pointsUpdater.shutdown())