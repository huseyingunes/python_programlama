import pyautogui

pyautogui.moveTo(799, 466, duration=2,
                 tween=pyautogui.easeInOutQuad)
pyautogui.click()
for i in range(100):
    pyautogui.write('Ne yazık ki evet!', interval=0.001)
    pyautogui.press('enter')
