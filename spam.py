import time, re, random
from pynput.keyboard import Key, Controller
randstring = False
keyboard = Controller()
time.sleep(2)
lyrics=[
    # "We're no strangers to love",
    # "You know the rules and so do I",
    # "A full commitment's what I'm thinking of",
    # "You wouldn't get this from any other guy",
    # "I just wanna tell you how I'm feeling",
    # "Gotta make you understand",
    # "Never gonna give you up",
    # "Never gonna let you down",
    # "Never gonna run around and desert you",
    # "Never gonna make you cry",
    # "Never gonna say goodbye",
    # "Never gonna tell a lie and hurt you",
    # "We've known each other for so long",
    # "------------------------"
    "@MUTED (Yea you can ping them as much as you like)"

]
while True:
    time.sleep(0.75)
    for line in lyrics:
        thingtosend = line
        # if randstring:
        #     thingtosend=re.sub(r'(...)', r'\1 ', thingtosend, random.randint(0, len(thingtosend)))
        for char in thingtosend:
            keyboard.press(char)
            time.sleep(0.01)
            keyboard.release(char)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    