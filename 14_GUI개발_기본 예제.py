from PyQt5.QtWidgets import *
import sys
from PyQt5 import uic
import os

ui_file = "./test.ui"
class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(ui_file, self)

        self.button.clicked.connect(self.showString)

    def showString(self):
        result = self.textinput.text()
        self.textoutput.setText(result)

QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())