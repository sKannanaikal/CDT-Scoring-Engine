import subprocess
import os
import signal

def play():
    timer = False
    p = subprocess.Popen(["C:/Program Files/Windows Media Player/wmplayer.exe", 'C:\\Users\\Sean Kannanaikal\\Documents\\CDT Scoring Engine\\nuke.mp4'])
    if timer == False:
        os.kill(p.pid, signal.SIGTERM)

play()