import pyautogui
from pynput.keyboard import Key, Controller, Listener
import keyboard
import time
songs = []
# keyboard = Controller()
# keyboard.press(Key.cmd)
# keyboard.press(Key.tab)
# keyboard.release(Key.tab)
# keyboard.release(Key.cmd)
# for i in range(0,len(songs)):
#     i = songs[i]
while True:
    if keyboard.is_pressed("iw"):
        print(pyautogui.position())
        break

