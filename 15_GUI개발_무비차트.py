from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import sys
from PyQt5 import uic
import os
from bs4 import BeautifulSoup
import urllib.request as req

ui_file = "./movie_chart.ui"
class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(ui_file, self)

        self.button.clicked.connect(self.showMovieChart)

    def showMovieChart(self):
        code = req.urlopen("http://www.cgv.co.kr/movies/")
        soup = BeautifulSoup(code, "html.parser")
        title = soup.select("div.sect-movie-chart strong.title")
        img = soup.select("span.thumb-image > img")  # 이미지 크롤링
        for i in range(len(title)):
            getattr(self, f"text{i+1}").setText(title[i].string)
            img_url = img[i].attrs["src"]
            data = req.urlopen(img_url).read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            pixmap = pixmap.scaled(185, 260)
            getattr(self, f"img{i+1}").setPixmap(pixmap)

QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())