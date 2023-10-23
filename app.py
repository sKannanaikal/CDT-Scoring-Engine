from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template, request
import atexit
import cv2
import time
import os
import signal
import subprocess

app = Flask(__name__)

houseofrepresentativesFlagContent = '' #update for all boxes
houseofrepresentativesFlagLocation = '' #update for all boxes
supremeCourtFlagContent = '' #update for all boxes
supremeCourtFlagLocation = '' #update for all boxes
federalReservesFlagContent = '' #update for all boxes
federalReservesFlagLocation = '' #update for all boxes
nationalArchivesFlagContent = '' #update for all boxes
nationalArchivesFlagLocation = '' #update for all boxes
federalTradeCommissionsFlagContent = '' #update for all boxes
federalTradeCommissionsFlagLocation = '' #update for all boxes
area51FlagContent = '' #update for all boxes
area51FlagLocation = '' #update for all boxes
pentagonFlagContent = '' #update for all boxes
pentagonFlagLocation = '' #update for all boxes
whiteHouseFlagContent = '' #update for all boxes
whiteHouseFlagLocation = '' #update for all boxes

houseofrepresentativesOwned = False
supremeCourtOwned = False
federalReservesOwned = False
nationalArchivesOwned = False
federalTradeCommissionsOwned = False
area51Owned = False
pentagonOwned = False
whiteHouseOwned = False

redTeamScore = 0
blueTeamScore = 0

blueColorHexCode = '#003cff'
redColorHexCode = '#ff0800'    

roundCount = 0


@app.route("/", methods = ['GET'])
def homePage():
    return render_template("index.html", redTeamScore=redTeamScore, blueTeamScore=blueTeamScore, redTeamColor=redColorHexCode, blueTeamColor=blueColorHexCode, 
                           roundCount=roundCount, houseofrepresentativesOwned=houseofrepresentativesOwned, supremeCourtOwned=supremeCourtOwned, federalReservesOwned=federalReservesOwned, nationalArchivesOwned=nationalArchivesOwned,
                           federalTradeCommissionsOwned=federalTradeCommissionsOwned, area51Owned=area51Owned, pentagonOwned=pentagonOwned, whiteHouseOwned=whiteHouseOwned)

@app.route("/flag", methods = ['POST'])
def ownershipToggle():
    global houseofrepresentativesOwned
    global supremeCourtOwned
    global federalReservesOwned
    global nationalArchivesOwned
    global federalTradeCommissionsOwned
    global area51Owned
    global pentagonOwned
    global whiteHouseOwned

    global houseofrepresentativesFlagContent
    global houseofrepresentativesFlagLocation
    global supremeCourtFlagContent
    global supremeCourtFlagLocation
    global federalReservesFlagContent
    global federalReservesFlagLocation
    global nationalArchivesFlagContent
    global nationalArchivesFlagLocation
    global federalTradeCommissionsFlagContent
    global federalTradeCommissionsFlagLocation
    global area51FlagContent
    global area51FlagLocation
    global pentagonFlagContent
    global pentagonFlagLocation
    global whiteHouseFlagContent
    global whiteHouseFlagLocation

    if request.method == 'POST':
        team = request.form['team']
        box = request.form['hostname']
        flagContent = request.form['flag']
        flagLocation = request.form['location']
        if box == 'houseofrepresentatives.us.gov':
            if team == 'blue':
                if houseofrepresentativesFlagContent != '' and houseofrepresentativesFlagLocation != '':
                    if flagContent == houseofrepresentativesFlagContent and flagLocation == houseofrepresentativesFlagLocation:
                        houseofrepresentativesFlagContent = ''
                        houseofrepresentativesFlagLocation = ''
                        houseofrepresentativesOwned = False
                        print('[+] Blue Team Removed Flag on machine')
                        return '[+] Blue Team Removed Flag on machine'
                    else:
                        return '[+] Try again seems like that was not correct'
            elif team == 'red':
                if houseofrepresentativesFlagContent != '' and houseofrepresentativesFlagLocation != '':
                    return '[+] Flag Already Exists on Machine'
                else:
                    houseofrepresentativesFlagContent = flagContent
                    houseofrepresentativesFlagLocation = flagLocation
                    houseofrepresentativesOwned = True
                    print(f'[+] Red team succesfully uploaded flag onto machine')
                    return f'[+] Red team succesfully uploaded flag onto machine'
        elif box == 'supremecourt.us.gov':
            if team == 'blue':
                if supremeCourtFlagContent != '' and supremeCourtFlagLocation != '':
                    if flagContent == supremeCourtFlagContent and flagLocation == supremeCourtFlagLocation:
                        supremeCourtFlagContent = ''
                        supremeCourtFlagLocation = ''
                        supremeCourtOwned = False
                        print('[+] Blue Team Removed Flag on machine')
                        return '[+] Blue Team Removed Flag on machine'
                    else:
                        return '[+] Try again seems like that was not correct'
            elif team == 'red':
                if supremeCourtFlagContent != '' and supremeCourtFlagLocation != '':
                    return '[+] Flag Already Exists on Machine'
                else:
                    supremeCourtFlagContent = flagContent
                    supremeCourtFlagLocation = flagLocation
                    supremeCourtOwned = True
                    print(f'[+] Red team succesfully uploaded flag onto machine')
                    return f'[+] Red team succesfully uploaded flag onto machine'
        elif box == 'federalreserves.us.gov':
            if team == 'blue':
                if federalReservesFlagContent != '' and federalReservesFlagLocation != '':
                    if flagContent == federalReservesFlagContent and flagLocation == federalReservesFlagLocation:
                        federalReservesFlagContent = ''
                        federalReservesFlagLocation = ''
                        federalReservesOwned = False
                        print('[+] Blue Team Removed Flag on machine')
                        return '[+] Blue Team Removed Flag on machine'
                    else:
                        return '[+] Try again seems like that was not correct'
            elif team == 'red':
                if federalReservesFlagContent != '' and federalReservesFlagLocation != '':
                    return '[+] Flag Already Exists on Machine'
                else:
                    federalReservesFlagContent = flagContent
                    federalReservesFlagLocation = flagLocation
                    federalReservesOwned = True
                    print(f'[+] Red team succesfully uploaded flag onto machine')
                    return f'[+] Red team succesfully uploaded flag onto machine'
        elif box == 'nationalarchives.us.gov':
            if team == 'blue':
                if nationalArchivesFlagContent != '' and nationalArchivesFlagLocation != '':
                    if flagContent == nationalArchivesFlagContent and flagLocation == nationalArchivesFlagLocation:
                        nationalArchivesFlagContent = ''
                        nationalArchivesFlagLocation = ''
                        nationalArchivesOwned = False
                        print('[+] Blue Team Removed Flag on machine')
                        return '[+] Blue Team Removed Flag on machine'
                    else:
                        return '[+] Try again seems like that was not correct'
            elif team == 'red':
                if nationalArchivesFlagContent != '' and nationalArchivesFlagLocation != '':
                    return '[+] Flag Already Exists on Machine'
                else:
                    nationalArchivesFlagContent = flagContent
                    nationalArchivesFlagLocation = flagLocation
                    nationalArchivesOwned = True
                    print(f'[+] Red team succesfully uploaded flag onto machine')
                    return f'[+] Red team succesfully uploaded flag onto machine'
        elif box == 'federaltradecommissions.us.gov':
            if team == 'blue':
                if federalTradeCommissionsFlagContent != '' and federalTradeCommissionsFlagLocation != '':
                    if flagContent == federalTradeCommissionsFlagContent and flagLocation == federalTradeCommissionsFlagLocation:
                        federalTradeCommissionsFlagContent = ''
                        federalTradeCommissionsFlagLocation = ''
                        federalTradeCommissionsOwned = False
                        print('[+] Blue Team Removed Flag on machine')
                        return '[+] Blue Team Removed Flag on machine'
                    else:
                        return '[+] Try again seems like that was not correct'
            elif team == 'red':
                if federalTradeCommissionsFlagContent != '' and federalTradeCommissionsFlagLocation != '':
                    return '[+] Flag Already Exists on Machine'
                else:
                    federalTradeCommissionsFlagContent = flagContent
                    federalTradeCommissionsFlagLocation = flagLocation
                    federalTradeCommissionsOwned = True
                    print(f'[+] Red team succesfully uploaded flag onto machine')
                    return f'[+] Red team succesfully uploaded flag onto machine'
        elif box == 'area51.us.gov':
            if team == 'blue':
                if area51FlagContent != '' and area51FlagLocation != '':
                    if flagContent == area51FlagContent and flagLocation == area51FlagLocation:
                        area51FlagContent = ''
                        area51FlagLocation = ''
                        area51Owned = False
                        print('[+] Blue Team Removed Flag on machine')
                        return '[+] Blue Team Removed Flag on machine'
                    else:
                        return '[+] Try again seems like that was not correct'
            elif team == 'red':
                if area51FlagContent != '' and area51FlagLocation != '':
                    return '[+] Flag Already Exists on Machine'
                else:
                    area51FlagContent = flagContent
                    area51FlagLocation = flagLocation
                    area51Owned = True
                    print(f'[+] Red team succesfully uploaded flag onto machine')
                    return f'[+] Red team succesfully uploaded flag onto machine'
        elif box == 'pentagon.us.gov':
            if team == 'blue':
                if pentagonFlagContent != '' and pentagonFlagLocation != '':
                    if flagContent == pentagonFlagContent and flagLocation == pentagonFlagLocation:
                        pentagonFlagContent = ''
                        pentagonFlagLocation = ''
                        pentagonOwned = False
                        print('[+] Blue Team Removed Flag on machine')
                        return '[+] Blue Team Removed Flag on machine'
                    else:
                        return '[+] Try again seems like that was not correct'
            elif team == 'red':
                if pentagonFlagContent != '' and pentagonFlagLocation != '':
                    return '[+] Flag Already Exists on Machine'
                else:
                    pentagonFlagContent = flagContent
                    pentagonFlagLocation = flagLocation
                    pentagonOwned = True
                    print(f'[+] Red team succesfully uploaded flag onto machine')
                    return f'[+] Red team succesfully uploaded flag onto machine'
        elif box == 'whitehouse': #might not have to update but check
            if team == 'blue':
                if whiteHouseFlagContent != '' and whiteHouseFlagLocation != '':
                    if flagContent == whiteHouseFlagContent and flagLocation == whiteHouseFlagLocation:
                        whiteHouseFlagContent = ''
                        whiteHouseFlagLocation = ''
                        whiteHouseOwned = False
                        print('[+] Blue Team Removed Flag on machine')
                        return '[+] Blue Team Removed Flag on machine'
                    else:
                        return '[+] Try again seems like that was not correct'
            elif team == 'red':
                if whiteHouseFlagContent != '' and whiteHouseFlagLocation != '':
                    return '[+] Flag Already Exists on Machine'
                else:
                    whiteHouseFlagContent = flagContent
                    whiteHouseFlagLocation = flagLocation
                    whiteHouseOwned = True
                    print(f'[+] Red team succesfully uploaded flag onto machine')  
                    return f'[+] Red team succesfully uploaded flag onto machine'        

def pointsUpdated():
    global redTeamScore
    global blueTeamScore
    global roundCount

    global houseofrepresentativesOwned
    global supremeCourtOwned
    global federalReservesOwned
    global nationalArchivesOwned
    global federalTradeCommissionsOwned
    global area51Owned
    global pentagonOwned
    global whiteHouseOwned

    if(houseofrepresentativesOwned):
        redTeamScore += 1
    else:
        blueTeamScore += 1

    if(supremeCourtOwned):
        redTeamScore += 1
    else:
        blueTeamScore += 1

    if(federalReservesOwned):
        redTeamScore += 1
    else:
        blueTeamScore += 1

    if(nationalArchivesOwned):
        redTeamScore += 1
    else:
        blueTeamScore += 1

    if(federalTradeCommissionsOwned):
        redTeamScore += 1
    else:
        blueTeamScore += 1

    if(area51Owned):
        redTeamScore += 1
    else:
        blueTeamScore += 1

    if(pentagonOwned):
        redTeamScore += 1
    else:
        blueTeamScore += 1

    if(whiteHouseOwned):
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
