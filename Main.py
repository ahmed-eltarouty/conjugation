from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5 import uic
import sys
# from os import path
import docx2txt
import os

winMain = uic.loadUiType("homeProject.ui")[0]  # load main page
conj = uic.loadUiType("conj.ui")[0]  # assign a second window to a variable
noun = uic.loadUiType("noun.ui")[0]
source = uic.loadUiType("source.ui")[0]

os.chdir("C:\\noojapply")
# if os.path.exists("result.ind"):
#   os.remove("result.ind")

# os.system('noojapply ar result.ind DIC.nod grammar.sft corpus.txt')
# os.system('noojapply ar res.ind INVALIDMAX.nod INVALIDMAX.sft zzw.txt')

ind= open("res.ind", "r",encoding='UTF8')

f = []
for x in ind:
    x.split('\n')
    f.append(x)
###### Detete last line ***** #########
f.pop(-1)


class MainApp(QMainWindow, winMain):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.But()

    def But(self):
        self.pushButton.clicked.connect(self.show_verbs)  # call for a def that open and hide
        self.pushButton_3.clicked.connect(self.show_noun)
        self.pushButton_2.clicked.connect(self.show_source)

    def show_verbs(self):
        self.newWindow = Conj()  # assign conj to a new window
        self.newWindow.show()  # show this window
        self.hide()  # hide current window

    def show_noun(self):
        self.newWindow = Noun()  # assign conj to a new window
        self.newWindow.show()  # show this window
        self.hide()  # hide current window

    def show_source(self):
        self.newWindow = Source()  # assign conj to a new window
        self.newWindow.show()  # show this window
        self.hide()  # hide current window

class Conj(QMainWindow, conj):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        # super(MainApp,self).__init__(parent)
        # QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI()
        self.Handel_Button()
        self.groupBox_2.hide()

    def Handel_UI(self):
        self.setWindowTitle('Download NooJ')

    def Handel_Button(self):
        self.pushButton.clicked.connect(self.last)
        # self.pushButton_2.clicked.connect(self.easy)
        self.comboBox_5.currentTextChanged.connect(self.combobox6)
        self.comboBox_8.currentTextChanged.connect(self.combobox8)
        self.comboBox_8.currentTextChanged.connect(self.easy)

    def combobox6(self):
        if self.comboBox_5.currentIndex() == 1:
            self.comboBox_6.removeItem(3)
        elif self.comboBox_5.currentIndex() == 0:
            self.comboBox_6.insertItem(3, "الأمر")

    def easy(self):
        self.tableWidget_2.clearContents()
        self.tableWidget.clearContents()
        if ((self.comboBox_5.currentIndex() == 0) and (self.comboBox_6.currentIndex() == 1)):
            # ma3loum madi
            self.ReadWordMa3loumMadi()
        if ((self.comboBox_5.currentIndex() == 0) and (self.comboBox_6.currentIndex() == 2)):
            # ma3loum modar3
            self.ReadWordMa3loumModar3()
        if ((self.comboBox_5.currentIndex() == 0) and (self.comboBox_6.currentIndex() == 3)):
            self.ReadWordMa3loumAmr()

        if ((self.comboBox_5.currentIndex() == 1) and (self.comboBox_6.currentIndex() == 1)):
            # majhoul madi
            self.ReadWordMajhoulMadi()
        if ((self.comboBox_5.currentIndex() == 1) and (self.comboBox_6.currentIndex() == 2)):
            # majhoul modar3
            self.ReadWordMajhoulModar3()

        if self.comboBox_5.currentIndex() == 0 and (self.comboBox_6.currentIndex() == 0):
            self.ReadWord()
        if self.comboBox_5.currentIndex() == 1 and (self.comboBox_6.currentIndex() == 0):
            self.ReadWord2()
        # if self.comboBox_5.currentIndex() == 4:
        #     self.ReadWord()
        #     self.ReadWord2()
        # self.last()
    def last(self):
        self.comboBox_8.clear()
        self.comboBox_7.clear()
        name = self.lineEdit.text()


        self.lines = []
        self.v=[]

        for x in f:
            if x != "" and x.split(',')[4].split('+')[2].replace('Root=','') == name:
                # print('ooooooooooook',x.split(',')[2].replace('<',''))
                self.lines.append(x)
                for line in self.lines:
                    if (line.split(',')[2].replace('<','') not in  self.v):
                         self.v.append(line.split(',')[2].replace('<',''))


        self.comboBox_8.addItems(self.v)
        # self.comboBox_7.addItems(m)
        

    ######################## Meanings combo box 7#######################
    ####################################################################
    def combobox8(self):
        self.comboBox_7.clear()
        m=[]
        for x in self.lines:
            if x.split(',')[2].replace('<','') == self.comboBox_8.currentText() and x.split(',')[4].split('+')[6] not in m:
                m.append(x.split(',')[4].split('+')[6])

        
        self.comboBox_7.addItems(m)

        
    def ReadWordMajhoulModar3(self):
        # self.comboBox_8.clear()
        self.groupBox.hide()
        self.groupBox_2.show()
        self.tableWidget_2.resizeColumnsToContents()

        # name = self.lineEdit.text()
        # my_text = docx2txt.process(name + ".docx")
        # lines= my_text.split('\n')

        v=[]
        m=[]
        for x in self.lines:
            if x != "" and x.split(',')[2].replace('<','') not in v and x.split(',')[4].split('+')[6] not in m:
                v.append(x.split(',')[2].replace('<',''))
                m.append(x.split(',')[4].split('+')[6])
                # self.lines.append(x)

        if self.comboBox_8.currentText() == "":
            self.comboBox_8.addItems(v)
        if self.comboBox_7.currentText() == "":
            self.comboBox_7.addItems(m)

        while True:
            for x in self.lines:
                if "Voix=K+Time=P+Pers=1+Nb=s" in x and self.comboBox_8.currentText() == line.split(',')[2].replace('<',''):
                    self.tableWidget_2.setItem(0, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(1, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(2, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(3, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(4, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(5, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(6, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(7, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(8, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(9, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(10, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(11, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(12, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(13, 2, QTableWidgetItem(x.split(',')[3]))
                    ########################################################################################################################
                    ########################################################################################################################
                if "Voix=K+Time=C+Pers=1+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(0, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=C+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(1, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=C+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(2, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=C+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(3, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=C+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(4, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=C+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(5, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=C+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(6, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=C+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(7, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=C+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(8, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=S+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(9, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=S+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(10, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=S+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(11, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=S+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(12, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=S+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(13, 1, QTableWidgetItem(x.split(',')[3]))
                    ########################################################################################################################
                    ########################################################################################################################                    if "+Voix=K+Time=P+Pers=1+Nb=s" in x:
                    self.tableWidget_2.setItem(0, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(1, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(2, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(3, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(4, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(5, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(6, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(7, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(8, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(9, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(10, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(11, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(12, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=P+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(13, 2, QTableWidgetItem(x.split(',')[3]))
                    ########################################################################################################################
                    ########################################################################################################################
                if "+Voix=K+Time=S+Pers=1+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(0, 3, QTableWidgetItem(x.split(',')[3]))
                if "+Voix=K+Time=S+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(1, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=S+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(2, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=S+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(3, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=S+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(4, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=S+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(5, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=S+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(6, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=S+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(7, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=S+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(8, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=S+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(9, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=S+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(10, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=S+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(11, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=S+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(12, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=S+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(13, 3, QTableWidgetItem(x.split(',')[3]))
                    ##########################################################################
                if "Voix=K+Time=B+Pers=1+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(0, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=B+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(1, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=B+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(2, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=B+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(3, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=B+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(4, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=B+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(5, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=B+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(6, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=B+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(7, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=B+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(8, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=B+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(9, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=B+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(10, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=B+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(11, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=B+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(12, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=B+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(13, 4, QTableWidgetItem(x.split(',')[3]))
            break

    def ReadWordMajhoulMadi(self):
        self.groupBox.hide()
        self.groupBox_2.show()
        self.tableWidget_2.resizeColumnsToContents()

        # name = self.lineEdit.text()
        # my_text = docx2txt.process(name + ".docx")
        # lines = my_text.split('\n')
        while True:
            for x in self.lines:
                if "Voix=K+Time=I+Pers=1+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(0, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=I+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(1, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=I+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(2, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=I+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(3, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=I+d+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(4, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=I+d+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(5, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=I+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(6, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=I+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(7, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=I+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(8, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=I+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(9, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=I+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(10, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=I+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(11, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=I+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(12, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=K+Time=I+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget_2.setItem(13, 0, QTableWidgetItem(x.split(',')[3]))
            break

    def ReadWordMa3loumMadi(self):
        self.groupBox_2.hide()  # majhoul
        self.groupBox.show()  # ma3loum
        # name = self.lineEdit.text()
        # my_text = docx2txt.process(name + ".docx")
        # lines = my_text.split('\n')
        
        while True:
            for x in self.lines:
                if "Voix=A+Time=I+Pers=1+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(0, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=I+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(1, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=I+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(2, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=I+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(3, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=I+Genre=m+Pers=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(4, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=I+Genre=f+Pers=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(5, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=I+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(6, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=I+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(7, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=I+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(8, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=I+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(9, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=I+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(10, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=I+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(11, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=I+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(12, 0, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=I+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(13, 0, QTableWidgetItem(x.split(',')[3]))
            break

    def ReadWordMa3loumModar3(self):
        self.groupBox_2.hide()  # majhoul
        self.groupBox.show()  # ma3loum
        # name = self.lineEdit.text()
        # my_text = docx2txt.process(name + ".docx")
        # lines = my_text.split('\n')
        while True:
            for x in self.lines:
                if "Voix=A+Time=S+Pers=1+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(0, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=S+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(1, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=S+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(2, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=S+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(3, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=S+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(4, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=S+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(5, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=S+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(6, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=S+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(7, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=S+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(8, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=S+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(9, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=S+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(10, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=S+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(11, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=S+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(12, 1, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=S+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(13, 1, QTableWidgetItem(x.split(',')[3]))
                ########################################################################################################################
                ########################################################################################################################
                if "Voix=A+Time=C+Pers=1+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(0, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=C+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(1, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=C+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(2, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=C+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(3, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=C+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(4, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=C+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(5, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(6, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=C+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(7, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=C+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(8, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=C+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(9, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=C+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(10, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=C+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(11, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=C+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(12, 2, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=C+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(13, 2, QTableWidgetItem(x.split(',')[3]))
                ########################################################################################################################
                ########################################################################################################################
                if "Voix=A+Time=P+Pers=1+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(0, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=P+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(1, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=P+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(2, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=P+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(3, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=P+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(4, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=P+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(5, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=P+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(6, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=P+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(7, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=P+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(8, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=P+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(9, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=P+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(10, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=P+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(11, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=P+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(12, 3, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=P+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(13, 3, QTableWidgetItem(x.split(',')[3]))
                ############################################################################
                if "Voix=A+Time=B+Pers=1+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(0, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=B+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(1, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=B+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(2, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=B+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(3, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=B+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(4, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=B+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(5, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=B+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(6, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=B+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(7, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=B+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(8, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=B+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(9, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=B+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(10, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=B+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(11, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=B+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(12, 4, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=B+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(13, 4, QTableWidgetItem(x.split(',')[3]))

            break

    def ReadWordMa3loumAmr(self):
        self.groupBox_2.hide()  # majhoul
        self.groupBox.show()  # ma3loum
        # name = self.lineEdit.text()
        # my_text = docx2txt.process(name + ".docx")
        # lines = my_text.split('\n')
        while True:
            for x in self.lines:

                ######################################################################################################
                if "Voix=A+Time=Y+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(2, 5, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=Y+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(3, 5, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=Y+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(4, 5, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=Y+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(5, 5, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=Y+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(6, 5, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=Y+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(7, 5, QTableWidgetItem(x.split(',')[3]))
                ######################################################################################################
                if "Voix=A+Time=Z+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(2, 6, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=Z+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(3, 6, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=Z+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(4, 6, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=Z+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(5, 6, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=Z+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(6, 6, QTableWidgetItem(x.split(',')[3]))
                if "Voix=A+Time=Z+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                    self.tableWidget.setItem(7, 6, QTableWidgetItem(x.split(',')[3]))
            break

    def ReadWord(self):
        try:
            self.groupBox_2.hide()  # majhoul
            self.groupBox.show()  # ma3loum
            # name = self.lineEdit.text()
            # my_text = docx2txt.process(name + ".docx")
            # lines = my_text.split('\n')
            while True:
                for x in self.lines:
                    if "Voix=A+Time=I+Pers=1+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(0, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=I+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(1, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=I+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(2, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=I+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(3, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=I+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(4, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=I+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(5, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=I+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(6, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=I+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(7, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=I+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(8, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=I+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(9, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=I+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(10, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=I+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(11, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=I+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(12, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=I+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(13, 0, QTableWidgetItem(x.split(',')[3]))
                    ########################################################################################################################
                    ########################################################################################################################
                    if "Voix=A+Time=S+Pers=1+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(0, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=S+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(1, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=S+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(2, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=S+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(3, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=S+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(4, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=S+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(5, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=S+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(6, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=S+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(7, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=S+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(8, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=S+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(9, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=S+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(10, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=S+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(11, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=S+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(12, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=S+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(13, 1, QTableWidgetItem(x.split(',')[3]))
                    ########################################################################################################################
                    ########################################################################################################################
                    if "Voix=A+Time=C+Pers=1+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(0, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=C+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(1, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=C+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(2, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=C+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(3, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=C+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(4, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=C+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(5, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=C+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(6, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=C+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(7, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=C+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(8, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=C+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(9, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=C+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(10, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=C+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(11, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=C+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(12, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=C+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(13, 2, QTableWidgetItem(x.split(',')[3]))
                    ########################################################################################################################
                    ########################################################################################################################
                    if "Voix=A+Time=P+Pers=1+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(0, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=P+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(1, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=P+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(2, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=P+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(3, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=P+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(4, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=P+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(5, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=P+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(6, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=P+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(7, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=P+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(8, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=P+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(9, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=P+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(10, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=P+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(11, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=P+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(12, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=P+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(13, 3, QTableWidgetItem(x.split(',')[3]))
                    ########################################################################################################################
                    ########################################################################################################################
                    if "Voix=A+Time=B+Pers=1+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(0, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=B+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(1, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=B+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(2, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=B+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(3, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=B+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(4, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=B+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(5, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=B+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(6, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=B+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(7, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=B+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(8, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=B+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(9, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=B+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(10, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=B+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(11, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=B+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(12, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=B+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(13, 4, QTableWidgetItem(x.split(',')[3]))

                    ######################################################################################################
                    if "Voix=A+Time=Y+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(2, 5, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=Y+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(3, 5, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=Y+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(4, 5, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=Y+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(5, 5, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=Y+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(6, 5, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=Y+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(7, 5, QTableWidgetItem(x.split(',')[3]))
                    ######################################################################################################
                    if "Voix=A+Time=Z+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(2, 6, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=Z+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(3, 6, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=Z+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(4, 6, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=Z+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(5, 6, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=Z+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(6, 6, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=A+Time=Z+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget.setItem(7, 6, QTableWidgetItem(x.split(',')[3]))

                break
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("رجاء ادخل فعل صحيح")
            msg.setInformativeText("This is additional information")
            msg.setWindowTitle("احذر")
            msg.setDetailedText("رجاء ادخل فعل صحيح")

    def ReadWord2(self):
        try:
            self.groupBox.hide()
            self.groupBox_2.show()
            self.tableWidget_2.resizeColumnsToContents()

            # name = self.lineEdit.text()
            # my_text = docx2txt.process(name + ".docx")
            # lines = my_text.split('\n')
            while True:
                for x in self.lines:
                    ##############################################

                    ##########################################
                    if "Voix=K+Time=I+Pers=1+Nb=s" in x  and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(0, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=I+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(1, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=I+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(2, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=I+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(3, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=I+Pers=d+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(4, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=I+Pers=d+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(5, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=I+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(6, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=I+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(7, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=I+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(8, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=I+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(9, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=I+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(10, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=I+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(11, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=I+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(12, 0, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=I+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(13, 0, QTableWidgetItem(x.split(',')[3]))
                    #######################################################################################################################
                    ########################################################################################################################
                    if "+Voix=K+Time=P+Pers=1+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(0, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(1, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(2, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(3, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(4, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(5, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(6, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(7, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(8, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(9, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(10, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(11, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(12, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(13, 2, QTableWidgetItem(x.split(',')[3]))
                    ########################################################################################################################
                    ########################################################################################################################
                    if "Voix=K+Time=C+Pers=1+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(0, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=C+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(1, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=C+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(2, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=C+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(3, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=C+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(4, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=C+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(5, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=C+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(6, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=C+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(7, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=C+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(8, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=S+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(9, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=S+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(10, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=S+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(11, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=S+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(12, 1, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=S+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(13, 1, QTableWidgetItem(x.split(',')[3]))
                        ########################################################################################################################
                        ########################################################################################################################                    if "+Voix=K+Time=P+Pers=1+Nb=s" in x:
                        self.tableWidget_2.setItem(0, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(1, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(2, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(3, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(4, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(5, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(6, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(7, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(8, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(9, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(10, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(11, 2, QTableWidgetItem(x.split(',')[3]))

                    if "Voix=K+Time=P+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(12, 2, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=P+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(13, 2, QTableWidgetItem(x.split(',')[3]))
                    ########################################################################################################################
                    ########################################################################################################################
                    if "+Voix=K+Time=S+Pers=1+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(0, 3, QTableWidgetItem(x.split(',')[3]))
                    if "+Voix=K+Time=S+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(1, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=S+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(2, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=S+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(3, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=S+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(4, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=S+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(5, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=S+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(6, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=S+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(7, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=S+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(8, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=S+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(9, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=S+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(10, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=S+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(11, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=S+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(12, 3, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=S+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(13, 3, QTableWidgetItem(x.split(',')[3]))
                    ##########################################################################
                    if "+Voix=K+Time=B+Pers=1+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(0, 4, QTableWidgetItem(x.split(',')[3]))
                    if "+Voix=K+Time=B+Pers=1+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(1, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=B+Pers=2+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(2, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=B+Pers=2+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(3, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=B+Genre=m+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(4, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=B+Genre=f+Nb=d" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(5, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=B+Pers=2+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(6, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=B+Pers=2+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(7, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=B+Pers=3+Genre=m+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(8, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=B+Pers=3+Genre=f+Nb=s" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(9, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=B+Pers=5+Genre=m" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(10, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=B+Pers=5+Genre=f" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(11, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=B+Pers=3+Genre=m+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(12, 4, QTableWidgetItem(x.split(',')[3]))
                    if "Voix=K+Time=B+Pers=3+Genre=f+Nb=p" in x and self.comboBox_8.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                        self.tableWidget_2.setItem(13, 4, QTableWidgetItem(x.split(',')[3]))

                break
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("رجاء ادخل فعل صحيح")
            msg.setInformativeText("This is additional information")
            msg.setWindowTitle("احذر")
            msg.setDetailedText("رجاء ادخل فعل صحيح")

class Noun(QMainWindow, noun):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.Hndl_Noun_Buttn()
        self.groupBox_2.hide()

    def Hndl_Noun_Buttn(self):
        self.pushB.clicked.connect(self.same_root)
        self.comboBox.currentTextChanged.connect(self.adj)
        self.comboBox_2.currentTextChanged.connect(self.meaning)
        self.comboBox_2.currentTextChanged.connect(self.show_data)
        self.comboBox_3.currentTextChanged.connect(self.sum)
        self.pushB_2.clicked.connect(self.show_sum)
        self.pushButton.clicked.connect(self.back_sum)
        self.comboBox_6.currentTextChanged.connect(self.sum_window)

    def back_sum(self):
        self.groupBox.show()
        self.groupBox_2.hide()
    def show_sum(self):
        self.same_root()
        self.groupBox.hide()
        self.groupBox_2.show()
        li=[]
        for x in self.means:
            if "bp" in x.split(',')[2].split('+') and x.split(',')[0] not in li:
                li.append(x.split(',')[0])
        self.comboBox_6.addItems(li)

    def same_root(self):
        self.comboBox.clear()
        noun1 = self.line.text()
        text = docx2txt.process(noun1 + ".docx")
        lines = text.split('\n')
        line = []
        self.means=[]
        i=0
        for x in lines :
            if x != "" and x!=" ":
                for n in range(len(x.split(',')[2].split('+'))):
                    if x.split(',')[2].split('+')[n] == noun1:
                        line.append(x)

        while i<len(line)-1:
            self.means.append(line[i])
            i += 6
        lines.clear()
        for x in self.means:
            if "bp" not in (x.split(',')[2].split('+')) and  (x.split(',')[1]) not in lines:
                lines.append(x.split(',')[1])

        self.comboBox.addItems(lines)
        self.adj()
        return (self.means)

    def adj(self):
        self.comboBox_2.clear()
        i=[]
        for x in self.means:
            if x.split(',')[1] == self.comboBox.currentText() and (x.split(',')[2].split('+')[0]) not in i:
                i.append(x.split(',')[2].split('+')[0])
        for x in i:
            if x == "N":
                self.comboBox_2.addItem("اسم")
            elif x == "ADJ":
                self.comboBox_2.addItem("صفة")
        # self.comboBox_2.addItems(i)
        i.clear()

    def meaning(self):
        self.comboBox_3.clear()
        w=self.comboBox.currentText()
        t=0
        if self.comboBox_2.currentText() == "اسم":
            t="N"
        elif self.comboBox_2.currentText() == "صفة":
            t="ADJ"
        # print(self.comboBox_2.currentText(),t)
        for x in self.means:
            if w == x.split(',')[1] and t == (x.split(',')[2].split('+')[0]) and "FLX" not in (x.split(',')[2].split('+')[6]) and "bp" not in (x.split(',')[2].split('+')):
                self.comboBox_3.addItem(x.split(',')[2].split('+')[6])
                # print(x)
        self.sum()
        self.show_data()
    def sum(self):
        m=[]
        self.comboBox_4.clear()
        for x in self.means:
            if "bp" in (x.split(',')[2].split('+')) and self.comboBox.currentText() == (x.split(',')[1]) and (x.split(',')[0]) not in m:
                m.append(x.split(',')[0])
        self.comboBox_4.addItems(m)

    def show_data(self):
        self.textB.clear()
        w=self.comboBox.currentText()
        # t=self.comboBox_2.currentText()
        m=self.comboBox_3.currentText()
        t=""
        if self.comboBox_2.currentText() == "اسم":
            t="N"
        elif self.comboBox_2.currentText() == "صفة":
            t="ADJ"
        for x in self.means:
            if (x.split(',')[1]) == w and "bp" not in (x.split(',')[2].split('+')) and (x.split(',')[2].split('+')[0]) == t and [(x.split(',')[2].split('+')[6]) == m or m == ""]:
                # self.textB.append(x.split(',')[2].split('+')[6])
                # print(x)
                for n in range(len(x.split(',')[2].split('+'))):
                    if x.split(',')[2].split('+')[n] == "N" :
                        self.textB.append("نوع الكلمة المدخلة هو : اسم  ")
                        self.textB.append("الوزن : " + x.split(',')[2].split('+')[3])
                    elif x.split(',')[2].split('+')[n] == "ADJ":
                        self.textB.append("نوع الكلمة المدخلة هو : صفة  ")
                        self.textB.append("الوزن : " + x.split(',')[2].split('+')[2])

                    if x.split(',')[2].split('+')[n] == "m" :
                        self.textB.append("جنس الكلمة المدخلة هو : مذكر   ")
                    elif x.split(',')[2].split('+')[n] == "f":
                        self.textB.append("جنس الكلمة المدخلة هو : مؤنث   ")
                    if x.split(',')[2].split('+')[n] == "Hum":
                        self.textB.append("دلالة الكلمة المدخلة : بشرى  ")
                    elif x.split(',')[2].split('+')[n] == "Null":
                        self.textB.append("دلالة الكلمة المدخلة : غير محدد  ")
                    elif x.split(',')[2].split('+')[n] == "Food":
                        self.textB.append("دلالة الكلمة المدخلة : طعام ")
                    elif x.split(',')[2].split('+')[n] == "Anml":
                        self.textB.append("دلالة الكلمة المدخلة : حيوان ")
                    elif x.split(',')[2].split('+')[n] == "Orgn":
                        self.textB.append("دلالة الكلمة المدخلة : عضو ")
                    if x.split(',')[2].split('+')[n] == "CCC":
                        self.textB.append("نوع الجذر : صحيح سالم  ")
                    elif x.split(',')[2].split('+')[n] == "CDD":
                        self.textB.append("نوع الجذر : مضاعف  ")

                self.textB.append("=====================")


    def sum_window(self):
        # self.same_root()
        self.comboBox_5.clear()
        self.textBrowser.clear()
        li=[]
        self.data=[]
        for x in self.means:
            if self.comboBox_6.currentText() == x.split(',')[0] and "bp" in x.split(',')[2].split('+') and x.split(',')[1] not in li:
                li.append(x.split(',')[1])
                self.data.append(x)
        self.comboBox_5.addItems(li)
        self.comboBox_5.currentTextChanged.connect(self.show_sum_data)
        self.show_sum_data()
    def show_sum_data(self):
        self.textBrowser.clear()
        for x in self.data:
            if self.comboBox_5.currentText() == x.split(',')[4].split('+')[4].replace('lemma="','').replace('"',''):
                self.textBrowser.append(" الوزن : "+ x.split(',')[2].split('+')[6])
                for n in range(len(x.split(',')[2].split('+'))):
                    if x.split(',')[2].split('+')[n] == "N":
                        self.textBrowser.append("نوع الكلمة المدخلة هو : اسم  ")
                    elif x.split(',')[2].split('+')[n] == "ADJ":
                        self.textBrowser.append("نوع الكلمة المدخلة هو : صفة  ")

                    if x.split(',')[2].split('+')[n] == "m":
                        self.textBrowser.append("جنس الكلمة المدخلة هو : مذكر   ")
                    elif x.split(',')[2].split('+')[n] == "f":
                        self.textBrowser.append("جنس الكلمة المدخلة هو : مؤنث   ")
                    if x.split(',')[2].split('+')[n] == "Hum":
                        self.textBrowser.append("دلالة الكلمة المدخلة : بشرى  ")
                    elif x.split(',')[2].split('+')[n] == "Null":
                        self.textBrowser.append("دلالة الكلمة المدخلة : غير محدد  ")
                    elif x.split(',')[2].split('+')[n] == "Food":
                        self.textBrowser.append("دلالة الكلمة المدخلة : طعام ")
                    elif x.split(',')[2].split('+')[n] == "Anml":
                        self.textBrowser.append("دلالة الكلمة المدخلة : حيوان ")
                    elif x.split(',')[2].split('+')[n] == "Orgn":
                        self.textBrowser.append("دلالة الكلمة المدخلة : عضو ")
                    if x.split(',')[2].split('+')[n] == "CCC":
                        self.textBrowser.append("نوع الجذر : صحيح سالم  ")
                    elif x.split(',')[2].split('+')[n] == "CDD":
                        self.textBrowser.append("نوع الجذر : مضاعف  ")

                self.textBrowser.append("=====================")





    def dicritic(self, dc):
        if dc == "an":
            return "تنوين بالفتح"
        if dc == "in":
            return "تنوين بالكسر"
        if dc == "un":
            return "تنوين بالضم"
        if dc == "a":
            return "فتحة"
        if dc == "i":
            return "كسرة"
        if dc == "u":
            return "ضمة"
    def root (self, root):
        if root == "CCC":
            return "صحيح سالم"
    def num(self,n):
        if n =="s":
            return "مفرد"
    def gender(self, gnd):
        if gnd == "m":
            return " مذكر"
        if gnd == "f":
            return " مؤنث"
    def semantic(self,sem):
        if sem =="Hum":
            return "إنسان"
    def noun_num(self,line,root):# يحسب كم كلمة موجودة في الملف تحمل
        i=0
        for x in line:
                if root in x:
                    i= i+1
        return ((i/2)-5) #

class Source(QMainWindow, source):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.but()

    def but(self):
        self.pushButton.clicked.connect(self.search)
        # self.comboBox.currentTextChanged.connect(self.details)


    def search(self):
        self.comboBox.clear()
        # os.chdir('F:\python\Projects\Illham')
        # my_text = docx2txt.process("verb-gerund.docx")
        # # text = docx2txt.process(noun1 + ".docx")
        # self.lines = my_text.split('\n')
        G=[]
        for x in f:
            if x != "" and x !=" " and x.split(',')[4].split('+')[0] == 'G' and self.lineEdit.text() == x.split(',')[2].replace('<','') and x.split(',')[3] not in G :
                G.append(x.split(',')[3])
                print(x.split(',')[3])
        self.comboBox.addItems(G)

    def details(self):
        self.textEdit.clear()
        for x in self.lines:
            if x != "" and x !=" " and self.comboBox.currentText() == x.split(',')[0] and x.split(',')[2].split('+')[0] == "G":
                self.textEdit.append(" المصدر : " + x.split(',')[2].split('+')[0])
                self.textEdit.append(" نوع المصدر : " + x.split(',')[2].split('+')[1])
                self.textEdit.append(" وزن المصدر : " + x.split(',')[2].split('+')[2])



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
