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
        # os.system('noojapply ar res.ind NooJ.nod INVALIDMAX.sft zzw.txt')  # call noojapply CMD
        ind = open("res.ind", "r",encoding='UTF8')
        Lines = ind.readlines()
        Lines.pop(-1)

        vrb = []



        for line in Lines:
            if (line.split(',')[2].replace('<','') not in vrb):
                vrb.append(line.split(',')[2].replace('<',''))


                        
        self.comboBox.addItems(vrb)

       
#############################  search with in x 




def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()