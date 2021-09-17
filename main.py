# Download the packages before running the code and making requied changes...
from base64 import decode                       
from PyQt5 import QtCore, QtGui, QtWidgets      
import array                                   
import random                                  
import pyqrcode                                
import png                                     
import password_strength as p                  
import time                                     
import pyperclip as pyp                        
import pandas as pd                            
from cryptography.fernet import Fernet

# ONLY EDIT THE CODE IF YOU ARE AWARE OF WHAT YOU ARE DOING 
#
# This class is for connecting the mongodb database and the GUI together.
class database():
    import pymongo 
    connection = pymongo.MongoClient('localhost', 27017)
    database=connection['project']
    collection = database['userdetails']
    def add(self,user,passw):
        self.collection.insert_one({'user':user,'password':passw}) 
        
        
# Dialog Box which displays Password
class Ui_PD(QtWidgets.QDialog):
    def __init__(self,pword):
        super().__init__()
        self.setObjectName("Dialog")
        self.setFixedSize(287, 169)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)
        self.setWindowOpacity(0.92)
        self.setStyleSheet("background-color:b")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(60, 10, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(60, 50, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:white;border:2 solid red ;border-radius:7;color:black")
        self.lineEdit.setFrame(True)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setText(pword)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(110, 110, 75, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color:white;border:2 solid red;border-radius:7")
        self.pushButton.setObjectName("pushButton")
        self.setWindowTitle("Password")
        self.label.setText("Password")
        self.lineEdit.setPlaceholderText("Password")
        self.pushButton.setText("Copy")
        self.pushButton.clicked.connect(self.clickcop)
    def clickcop(self):
        pyp.copy(self.lineEdit.text())
        
# "Save as" dialog box 
class Ui_SaveWindow(QtWidgets.QMainWindow):
    import pymongo
    connection = pymongo.MongoClient('localhost', 27017)
    database=connection['project']
    collection = database['userdetails']
    db=pd.DataFrame(collection.find())
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('img.png'))
        self.setObjectName("MainWindow")
        self.setFixedSize(300, 360) 
        self.setWindowTitle('Saved Passwords')
        self.setWindowOpacity(0.92)
        self.setStyleSheet('background-color:black')
        self.label=QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0,0,300,60))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText('Saved Accounts')
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:black;color:white")
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(0, 80, 300, 250))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setStyleSheet("background-color:black;color:skyblue;")
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2=QtWidgets.QLabel(self)
        self.label_2.setText('No saved passwords')
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setGeometry(QtCore.QRect(0,100,300,60))
        self.label_2.setStyleSheet("background-color:black;color:white")
        font.setPointSize(15)
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.tableWidget.setVisible(False)
        if(self.collection.count_documents({})>0):
            self.update()
            self.tableWidget.setVisible(True)
            self.label_2.setVisible(False)
            self.tableWidget.verticalHeader().setDefaultSectionSize(45)
            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.setObjectName("tableWidget")
            self.tableWidget.setRowCount(self.db.shape[0])
            self.tableWidget.setAutoScroll(True)
            for i in range(self.db.shape[0]):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(i, 0, item)
                font = QtGui.QFont()
                font.setPointSize(15)
                item.setFont(font)
                item.setText(str(self.db.iloc[i,1]))
                self.tableWidget.currentIndex()
        self.tableWidget.cellClicked.connect(self.click)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(300)
    def click(self):
        pword=str(self.db.iloc[self.tableWidget.currentRow(),self.tableWidget.currentColumn()+2])
        pword=bytes(pword,'utf-8')
        key=b'_yCm2EbK16FgwUOhNOC5Qy1kQ5TA4sE-auC6UrBFkNk='
        f = Fernet(key)
        tok=f.decrypt(pword)
        tok=tok.decode('utf-8')    
        ui=Ui_PD(str(tok))
        ui.exec()

#Strength Detector Window

class Ui_Dindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(360, 360)
        MainWindow.setStyleSheet("background-color:black")
        MainWindow.setWindowOpacity(0.92)
        MainWindow.setWindowIcon(QtGui.QIcon('password.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:lightblue;border: 2 solid red ;border-radius:10")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 190, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setVisible(False)
        self.label_2.setStyleSheet("color :white")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 80, 191, 31))
        self.lineEdit.setClearButtonEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:white;color:black;border-radius:10")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(36, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 230, 291, 21))
        self.progressBar.setStyleSheet("color:black;background-color:white;;border:2 solid red")
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(80)
        self.progressBar.setVisible(False)
        self.progressBar.setTextVisible(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 270, 120, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setVisible(False)
       
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Check your password here"))
        self.pushButton.setText(_translate("MainWindow", "Check"))
        self.label_2.setText(_translate("MainWindow", "Your password is"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Type your password..."))
        self.label.setText(_translate("MainWindow", "Strong Password or Not "))
        self.label_3.setText(_translate("MainWindow", ""))
        self.pushButton.clicked.connect(self.strength)
    def strength(self):
        s=self.lineEdit.text()
        if(s==''):
            self.progressBar.setVisible(False)
            self.label_2.setVisible(False)
            self.label_3.setVisible(False)
            m=QtWidgets.QMessageBox()
            m.setText('No password typed')
            m.setIcon(QtWidgets.QMessageBox.Warning)
            m.setWindowTitle('Error')
            m.exec_()
        else:
            self.label_2.setVisible(True)
            self.label_3.setVisible(True)
            self.progressBar.setVisible(True)
            stat=p.PasswordStats(s)
            a=int(stat.strength()*100)
            if(0<=a and a<=20):
                self.label_3.setStyleSheet("color:red;")
                self.label_3.setText("Very Weak")
            elif(20<a and a<30):
                self.label_3.setStyleSheet("color:yellow;")
                self.label_3.setText("  Weak")
            elif(30<=a and a<55):
                self.label_3.setText(" Strong")
                self.label_3.setStyleSheet("color:lightgreen;")
            elif(55<=a and a<80):
                self.label_3.setText("Very Strong")
                self.label_3.setStyleSheet("color:green")
            elif(80<=a):
                self.label_3.setText("Unbreakable")
                self.label_3.setStyleSheet("color:darkgreen;")
            for i in range((a+1)):
                time.sleep(0.01)
                self.progressBar.setValue(i)          
                self.label_3.adjustSize()
 # Function that generates passowrd of selected size
def password(i): 
    MAX_LEN = i
    p= ""
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']
    
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']
    
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
            '*', '(', ')', '<']
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
   
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
    
   
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
    for x in temp_pass_list:
            p = p + x
    return p 
  
 # GUI of HomeWindow
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(360,360)
        MainWindow.setStyleSheet('background-color:black')
        MainWindow.setWindowOpacity(0.92)
        MainWindow.setWindowIcon(QtGui.QIcon('password.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(300, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(8)
        self.spinBox.setMaximum(18)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setStyleSheet('color:black;background-color:white')
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet('color:white')
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 80, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet('color:skyblue;border:2 solid red;border-radius:7')
        self.lineEdit=QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setGeometry(QtCore.QRect(90,130,170,30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setFrame(True)
        self.lineEdit.setStyleSheet('background-color:white;color:black;border-radius:10')
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton_1=QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(80,190,80,30))
        self.pushButton_1.setStyleSheet('color:skyblue;border:2 solid red;border-radius:7')
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2=QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270,125,40,40))
        self.pushButton_2.setStyleSheet('color:white;border:2 solid red;border-radius:20')
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.savebutton=QtWidgets.QPushButton(self.centralwidget)
        self.savebutton.setGeometry(QtCore.QRect(190,190,80,30))
        self.savebutton.setStyleSheet('color:skyblue;border:2 solid red;border-radius:7')
        self.savebutton.setFont(font)
        self.label_2=QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100,170,160,160))
        self.label_2.setPixmap(QtGui.QPixmap("img.png"))
        self.label_2.setStyleSheet('border-radius:80')
        self.label_2.setWindowOpacity(0.8)
        self.label_2.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.pushButton_1.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.savebutton.setVisible(False)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
   
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Generator"))
        self.label.setText(_translate("MainWindow", "Number of characters in a password:"))
        self.pushButton.setText(_translate("MainWindow", "Generate"))
        self.pushButton.clicked.connect(self.click)
        self.pushButton_1.setText(_translate("MainWindow", "QR code"))
        self.pushButton_1.clicked.connect(self.click_qr)
        self.pushButton.setShortcut("Return")
        self.pushButton_2.setText('Copy')
        self.savebutton.setText('Save')
        self.pushButton_2.clicked.connect(self.copy)
        self.savebutton.clicked.connect(self.save)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.savebutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lineEdit.setPlaceholderText(_translate('MainWindow','Password'))
    def click(self):
        self.lineEdit.setText(password(self.spinBox.value()))
        self.label_2.setVisible(False)
        self.pushButton_2.setVisible(True)
        self.pushButton_1.setVisible(True)
        self.savebutton.setVisible(True)
    def click_qr(self):
        s=self.lineEdit.text()
        url = pyqrcode.create(s)
        url.png('myqr.png', scale=10)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.exec()
    def copy(self):
        pyp.copy(self.lineEdit.text())
    def save(self):
            saveD = Ui_Save(self.lineEdit.text())
            saveD.exec()

# QR code dispkay window.
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(302, 315)
        Dialog.setStyleSheet('background-color:black')
        Dialog.setWindowOpacity(0.92)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet('color:white')
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 161, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("myqr.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "QR Code"))
        self.label.setText(_translate("Dialog", "Scan the QR Code for Password"))
        self.label.adjustSize()
       
#Login Window of the Application
class Ui_Mainwindow(object):
    def setupUi(self, Mainwindow):
        Mainwindow.setObjectName("Mainwindow")
        Mainwindow.setWindowModality(QtCore.Qt.ApplicationModal)
        Mainwindow.setFixedSize(400, 400)
        Mainwindow.setTabletTracking(False)
        Mainwindow.setWindowOpacity(0.92)
        Mainwindow.setAutoFillBackground(False)
        Mainwindow.move(800,150)
        Mainwindow.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.label = QtWidgets.QLabel(Mainwindow)
        self.label.setGeometry(QtCore.QRect(190, 50, 71, 51))
        self.label.setStyleSheet("color:white; font-size:20pt;")
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.imag=QtWidgets.QLabel(Mainwindow)
        self.imag.setGeometry(QtCore.QRect(110,30,80,80))
        self.imag.setPixmap(QtGui.QPixmap("login.png"))
        self.imag.setStyleSheet('border-radius:40;background-color:black')
        self.opacity=QtWidgets.QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.7)
        self.imag.setGraphicsEffect(self.opacity)
        self.imag.setScaledContents(True)
        self.lineEdit = QtWidgets.QLineEdit(Mainwindow)
        self.lineEdit.setGeometry(QtCore.QRect(80, 130, 250, 35))
        self.lineEdit.setStyleSheet("font-size:11pt;background-color:white;color:black;border-radius:10")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setFrame(True)
        self.lineEdit_2 = QtWidgets.QLineEdit(Mainwindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 200, 250, 35))
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setStyleSheet("font-size:11pt;background-color:white;color:black;border-radius:10")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.pushButton = QtWidgets.QPushButton(Mainwindow)
        self.pushButton.setGeometry(QtCore.QRect(150,300, 120, 35))
        self.pushButton.setStyleSheet('background-color:black;color:lightblue;border:2 solid red;border-radius:7')
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setDefault(True)
        font=QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.clicked.connect(self.click)
        
        self.retranslateUi(Mainwindow)
        QtCore.QMetaObject.connectSlotsByName(Mainwindow)
    def click(self):
        if(self.lineEdit.text()=='admin'and self.lineEdit_2.text()=='password'):
            Mainwindow.close()
            self.MainWindow2 = QtWidgets.QMainWindow()
            self.ui2 = Ui_Window()
            self.ui2.setupUi(self.MainWindow2)
            self.MainWindow2.show()
        else :
            self.show_pop()
    def show_pop(self):
        m=QtWidgets.QMessageBox()
        m.setWindowTitle('Invalid Login')
        m.setText('Username or Password is Invalid')
        m.setIcon(QtWidgets.QMessageBox.Warning)
        m.setStyleSheet('color:white;background-color:black')
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        x=m.exec_()

    def retranslateUi(self, Mainwindow):
        _translate = QtCore.QCoreApplication.translate
        Mainwindow.setWindowTitle(_translate("Mainwindow", "Password-Generator"))
        Mainwindow.setWindowIcon(QtGui.QIcon('login.png'))
        self.label.setText(_translate("Mainwindow", "Login"))
        self.pushButton.setShortcut("Return")       
        self.pushButton.setText(_translate("Mainwindow", "Enter"))
        self.lineEdit_2.setPlaceholderText(_translate("Mainwindow",'Password...'))
        self.lineEdit.setPlaceholderText(_translate('Mainwindow','Username...'))

# Opion Window.
class Ui_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(280,300)
        MainWindow.setStyleSheet('background-color:black')
        MainWindow.setWindowOpacity(0.92)
        MainWindow.move(800,150)
        MainWindow.setWindowIcon(QtGui.QIcon('option.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 60, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color : lightblue ; border : 2 solid red;border-radius:20")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 130, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("color : lightblue ; border : 2 solid red;border-radius:20")
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 200, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("color : lightblue ; border : 2 solid red;border-radius:20")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def genrator(self):
        self.w=Windows()
        self.w.genwin()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Choose an option..."))
        self.pushButton.setText(_translate("Form", "Generator"))
        self.pushButton_2.setText(_translate("Form", "Saved Passwords"))
        self.pushButton_2.setShortcut(_translate("Form", "Return"))
        self.pushButton_3.setText(_translate("Form", "Strength Tester"))
        self.pushButton.clicked.connect(self.genrator)
        self.pushButton_2.clicked.connect(self.manager)
        self.pushButton_3.clicked.connect(self.detector)
    def manager(self):
        self.w=Windows()
        self.w.savedwin()
    def detector(self):
        self.w=Windows()
        self.w.decwin()
class Windows(object):
    def genwin(self):
        self.Mwindow=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.Mwindow)
        self.Mwindow.show()
    def decwin(self):
        self.mwindow=QtWidgets.QMainWindow()
        self.u=Ui_Dindow()
        self.u.setupUi(self.mwindow)
        self.mwindow.show()
    def savedwin(self):
        self.ui = Ui_SaveWindow()
        self.ui.show()
        
# Pasword-Manager window.
class Ui_Save(QtWidgets.QDialog):
    def __init__(self,txt):
        super().__init__()
        self.setObjectName("Dialog")
        self.setFixedSize(384, 196)
        self.setWindowOpacity(0.92)
        self.setStyleSheet('background-color:black')
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet('color:white')
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(90, 30, 161, 31))
        self.lineEdit.setStyleSheet("color:black;background-color:white;border-radius:7")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 81, 21))
        self.label_2.setStyleSheet('color:white')
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setText(txt)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 90, 161, 31))
        self.lineEdit_2.setStyleSheet("color:black;background-color:white;border-radius:7")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(190, 160, 75, 23))
        self.pushButton.setStyleSheet("color:white;background-color:black;border: 2 solid white ;border-radius:7")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 160, 75, 23))
        self.pushButton_2.setStyleSheet("color:white;background-color:black;border:2 solid white;border-radius:7")
        self.pushButton_2.setObjectName("pushButton_2")
        self.setWindowTitle("Save as")
        self.label.setText ("Save For :")
        self.lineEdit.setPlaceholderText("Gmaiil,Facebook,etc...")
        self.label_2.setText("Password :")
        self.pushButton.setText( "Ok")
        self.pushButton_2.setText("Cancel")
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.sava)
    def sava(self):
        if(self.lineEdit.text()==''):
            m=QtWidgets.QMessageBox()
            m.setWindowTitle('Invalid')
            m.setIcon(QtWidgets.QMessageBox.Warning)
            m.setText('Save For is not defined')
            x=m.exec_()
        else:
          ### This is the Cryptographic part of the code ###
            info=database()
            key=b'_yCm2EbK16FgwUOhNOC5Qy1kQ5TA4sE-auC6UrBFkNk='
            f = Fernet(key)
            t=bytes(self.lineEdit_2.text(),'utf-8')
            pword=f.encrypt(t)
            pword=pword.decode('utf-8')
            info.add(self.lineEdit.text(),pword)
            self.close()
# Code to run the GUI on Python.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mainwindow = QtWidgets.QMainWindow()
    ui = Ui_Mainwindow()
    ui.setupUi(Mainwindow)
    Mainwindow.show()
    sys.exit(app.exec_())
