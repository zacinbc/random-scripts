import time
from pynput.keyboard import Key, Controller
keyboard = Controller()
time.sleep(2)
currentnum=0
currentnumstr=""
while True:
    time.sleep(0.75)
    currentnum=currentnum+1
    currentnumstr=str(currentnum)
    for char in currentnumstr:
        keyboard.press(char)
        time.sleep(0.01)
        keyboard.release(char)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)