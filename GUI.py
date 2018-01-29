import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#Mainly just playing around with PyQt, only some of this will actually be used in real program
class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('Client Search')

        extractAction = QAction("Quit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Close Application")
        extractAction.triggered.connect(self.close_application)

        edit = QAction("&I Don't Do Anything", self)
        edit.setShortcut("Ctrl+W")
        edit.setStatusTip("Nothing, I tell you!")
        edit.triggered.connect(self.nothing)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        editMenu = mainMenu.addMenu('&Edit')
        editMenu.addAction(edit)

        self.home()

    def nothing(self):
        QMessageBox.information(self, "Not a Single Thing",
                                "NOTHING!!!")
    def home(self):
        btn = QPushButton('quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0, 100)
        self.show()

    def close_application(self):
        close = QMessageBox.question(self, "Close Application?",
                                     "Are you sure you want to close the application?",
                                     QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            sys.exit()
        else:
            pass

def run():
    app = QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())

run()
