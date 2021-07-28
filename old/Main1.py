from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5 import uic
import sys
# from os import path
import docx2txt
import os

winMain = uic.loadUiType("Main.ui")[0]  # load main page
Verb = uic.loadUiType("Verb.ui")[0]  # assign a second window to a variable





class MainApp(QMainWindow, winMain):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.But()
    
    


    def But(self):
        self.pushButton_2.clicked.connect(self.show_verbs)  # call for a def that open and hide
        



    def show_verbs(self):
        self.newWindow = Verb()  # assign conj to a new window
        self.newWindow.show()  # show this window
        self.hide()  # hide current window
        global name
        name = self.lineEdit.text()



class Verb(QMainWindow, Verb):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.but()

    def but(self):
        self.commandLinkButton.clicked.connect(self.search)
        # self.search()


    def search(self):
        os.chdir("C:\\noojapply")
        ind= open("res.ind", "r",encoding='UTF8')

        f = []
        for x in ind:
            x.split('\n')
            f.append(x)
        ###### Detete last line ***** #########
        f.pop(-1)

        self.comboBox.clear()

        V=[]
        for x in f:
            if x != "" and x !=" " :
                if x.split(',')[4].split('+')[0] == 'V' and name == x.split(',')[4].split('+')[3].replace('Root=','') and x.split(',')[3] not in V :
                    if 'Voix=A+Time=I+Pers=3+Genre=f+Nb=s' in x:
                        print(x)
                    
                    # if x.split(',')[4].split('+')[7] == 'Voix=A' and x.split(',')[4].split('+')[8] == 'Time=I' and x.split(',')[4].split('+')[9] == 'Pers=3' and x.split(',')[4].split('+')[10] == 'Genre=f' and x.split(',')[4].split('+')[11] == 'Nb=s>':
                        V.append(x.split(',')[3])
                        
        self.comboBox.addItems(V)

       
#############################  search with in x 




def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()