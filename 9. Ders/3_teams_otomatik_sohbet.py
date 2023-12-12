import pyautogui

CLICK = pyautogui.click()
import time

pyautogui.keyDown('alt')
time.sleep(.2)
pyautogui.press('tab')
time.sleep(.2)
pyautogui.keyUp('alt')
time.sleep(.2)

pyautogui.moveTo(1109, 909, duration=1,
                 tween=pyautogui.easeInOutQuad)
pyautogui.click()
for i in range(100):
    pyautogui.write('Yerine birine imza attirmak demek! Yoklamadan kaldin... Seneye gorusuruz...', interval=0.001)
    pyautogui.press('enter')
