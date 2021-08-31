from PyQt5 import QtGui, QtWidgets, QtCore
import sys, threading, winsound
import home,red , yellow, green

ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def mainUi():
    global ui
    playS("sound/Button_1_down.wav", 0)
    playS("sound/1.wav", 1)
    ui = home.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.button_red.clicked.connect(red_UI)
    ui.button_yellow.clicked.connect(yellow_UI)
    ui.button_green.clicked.connect(green_UI)
    MainWindow.show()

def red_UI():
    global ui
    playS("sound/Button_1_down.wav", 0)
    playS("sound/2.wav", 1)
    ui = red.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.back.clicked.connect(mainUi)
    MainWindow.show()
def yellow_UI():
    playS("sound/Button_1_down.wav", 0)
    playS("sound/2.wav", 1)
    global ui
    ui = yellow.Ui_MainWindow() 
    ui.setupUi(MainWindow)
    ui.back.clicked.connect(mainUi)
    MainWindow.show()

def green_UI():
    global ui
    playS("sound/Button_1_down.wav", 0)
    playS("sound/2.wav", 1)
    ui = green.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.back.clicked.connect(mainUi)
    MainWindow.show()


#a sẽ là bản nhạc muốn truyền .wav   . 
#b truyền vào 0 hoặc 1 . 0: chỉ chạy 1 lần không lặp lại; 1: chạy lặp lại
def Funtion_playsound(a, b): 
    winsound.PlaySound(a, winsound.SND_LOOP + (winsound.SND_ASYNC & b))
def playS(a, b):
    s = threading.Thread(target=Funtion_playsound, args=(a, b))
    s.start()



mainUi()
sys.exit(app.exec_())