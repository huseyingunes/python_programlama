import pyautogui

# Ekran Çözünürlüğü
screenWidth, screenHeight = pyautogui.size()
print("Ekran Çzözünürlüğü :", screenWidth, screenHeight)

# Fare Pozisyonu
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)


