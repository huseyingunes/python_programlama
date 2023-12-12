"""
Bir tkinkter penceresi oluşturun
Pencere başlığı Tıklayamazsın olsun.
Bu penzerenin üst orta kısmına Merhaba GUI yazdırın
Altına bir tane düğme ekleyin
Düğme de kapat yazsın.
Düğmenin üstüne gelinmesini pyautogui ile engelleyin.
    Tam üstüne gelinirken ekranda düğmenin olmadığı
    bir noktaya fareyi ışınlayın
Düğmenin altına bir lable daha ekleyin.
    Kişi her düğmeye yaklaşığ uzaklaştırıldığında
        Beceriksiz yazdırın...
"""


from tkinter import *
import random
import pyautogui

window = Tk()
window.title("Tıklayamazsın")
lbl = Label(window, text="Merhaba GUI")
lbl.place(relx=0.5, rely=0.1, anchor=CENTER)

lbl2 = Label(window, text="Durum")
lbl2.place(relx=0.5, rely=0.4, anchor=CENTER)

dgm = Button(window,
             text="KAPAT",
             width=20,
             height=3,
             bg="red")
dgm.place(relx=0.5, rely=0.25, anchor=CENTER)

def motion(event):
        screenWidth, screenHeight = pyautogui.size()
        pyautogui.moveTo(random.randint(0, screenWidth),
                         random.randint(0, screenHeight),
                         duration=0,
                         tween=pyautogui.easeInOutQuad)
        lbl2.configure(text="Tıklayamadı ki :D")

dgm.bind('<Motion>', motion)

window.geometry('500x400')
window.mainloop()