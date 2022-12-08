# https://pyautogui.readthedocs.io/en/latest/#
'''
Fare ve klavye kontrolü kütüphanesi
'''
import pyautogui

pyautogui.moveTo(500, 500, duration=2,
                 tween=pyautogui.easeInOutQuad)
pyautogui.moveTo(1000, 1000, duration=2,
                 tween=pyautogui.easeInCirc)
pyautogui.moveTo(50, 50, duration=2,
                 tween=pyautogui.easeInBounce)
pyautogui.moveTo(500, 500, duration=2,
                 tween=pyautogui.easeOutElastic)