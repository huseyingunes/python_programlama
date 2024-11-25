import pandas as pd
import pyautogui
import time

pyautogui.moveTo(590, 420)
pyautogui.keyDown('alt')
time.sleep(.2)
pyautogui.press('tab')
time.sleep(.2)
pyautogui.keyUp('alt')
time.sleep(.2)
pyautogui.click()
time.sleep(.4)

# Excel dosyasını oku
df = pd.read_excel('ogrenci_listesi.xls')

for numara in df.itertuples():
    pyautogui.write(str(numara[1]), interval=0.001)
    time.sleep(7)
    pyautogui.press('enter')
    time.sleep(3)


