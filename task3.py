#!python3
import pyautogui
import time

kim= 29
x,y = pyautogui.locateCenterOnScreen('assets/redarrow.png', confidence=0.9)
pyautogui.moveTo(x,y)
pyautogui.moveTo(x+kim*3,y,)
pyautogui.moveTo(x+kim*3,y+kim*3)
pyautogui.moveTo(x+kim*2,y+kim*3)
pyautogui.moveTo(x+kim*2,y+kim*7)
pyautogui.moveTo(x+kim*4,y+kim*7)
pyautogui.moveTo(x+kim*4,y+kim*6)
pyautogui.moveTo(x+kim*3,y+kim*6)
pyautogui.moveTo(x+kim*3,y+kim*4)
pyautogui.moveTo(x+kim*5,y+kim*4)
pyautogui.moveTo(x+kim*5,y+kim*2)
pyautogui.moveTo(x+kim*7,y+kim*2)
pyautogui.moveTo(x+kim*7,y+kim)
pyautogui.moveTo(x+kim*9,y+kim)
pyautogui.moveTo(x+kim*9,y+kim*3)
pyautogui.moveTo(x+kim*7,y+kim*3)
pyautogui.moveTo(x+kim*7,y+kim*6)
pyautogui.moveTo(x+kim*6,y+kim*6)
pyautogui.moveTo(x+kim*6,y+kim*9)
pyautogui.moveTo(x+kim*8,y+kim*9)
pyautogui.moveTo(x+kim*8,y+kim*8)
pyautogui.moveTo(x+kim*13,y+kim*8)


