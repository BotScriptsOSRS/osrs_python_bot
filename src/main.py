from utilities import TakeBreak, data
from tanning_bot import TanBot, Hide
import time 
import random
from utilities.object_detection import ObjectDetection
from walker.path_enum import Path
from walker.walking import Walking

# hide = Hide.COW_HIDE.value
# tanned_hide = Hide.HARD_LEATHER.value

# breaker = TakeBreak()
# tan_bot = TanBot(hide, tanned_hide)


# breaker.login()
# python src/utilities/server.py
# pip install simplejson numpy pywin32 pyautogui opencv-python pillow
walker = Walking(data, ObjectDetection)

def main():
    path = Path.GE_CIRCLE.value
    walker.walk(path)

    # time_start = time.time()
    # time_duration_min = random.randint(120, 180)

    # while True:
    #     # Run script for 2 to 3 hours.
    #     while time.time() < time_start + time_duration_min*60:
    #         tan_bot.run()
    #     tan_bot.inv_open = False
    #     # Take a break of 5 to 15 minutes.
    #     breaker.take_break()
    #     time_start = time.time()

if __name__ == '__main__':
    main()
    
