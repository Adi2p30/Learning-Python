import pyautogui
import keyboard
import time
# while True:
#     p = pyautogui.position()
#     x = p.x
#     y= p.y
#     if keyboard.is_pressed('i'):
#         print(pyautogui.position())
#         break
#  Search bar  Point(x=906, y=179)
#  Save button Point(x=1173, y=961)
#  Play video  Point(x=669, y=66i4)
#  PLaylist    Point(x=953, y=637)
#  Compose     Point(x=148, y=302)
#  send button Point(x=1193, y=1002)
#  Subject     Point(x=1224, y=518)
#  email       Point(x=1231, y=578)
#reeni.ghoshal@sanskritischoolpune.org
#____________________________________________________
# pyautogui.click(243,1059)
# pyautogui.press("alt")
# pyautogui.press("tab")
# pyautogui.click(1536,104)
# pyautogui.typewrite("waves")
# pyautogui.press("enter")
#_______________________________________________
import pyautogui
import keyboard


def emailspam():
    x = 10
    while True:
        if keyboard.is_pressed('i'):
            for i in range(0,x):
                pyautogui.click(148,302)
                time.sleep(0.5)
                pyautogui.typewrite("ananya.dongsarwar@smspune.in")
                time.sleep(0.4)
                pyautogui.click(1713, 523)
                pyautogui.typewrite("I HATE YOU")
                time.sleep(0.4)
                pyautogui.click(1231,578)
                pyautogui.typewrite("why are you so smart >_<")
                time.sleep(0.4)
                pyautogui.click(1193,1002)
                time.sleep(0.5)
def penguinsave():
    x = 50
    while True:
        if keyboard.is_pressed('i'):
            for i in range(0, x):
                time.sleep(0.6)
                pyautogui.typewrite("Save the penguins 🐧")
penguinsave()