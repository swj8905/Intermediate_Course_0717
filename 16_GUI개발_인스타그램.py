from PyQt5.QtWidgets import *
import sys
from PyQt5 import uic
import os
import chromedriver_autoinstaller
from selenium import webdriver
from PyQt5.QtCore import QThread, QObject, pyqtSignal
from PyQt5.QtGui import QPixmap
import time
import random
import urllib.request as req



ui_file = "./instagram.ui"

class SeleniumWorker(QObject):
    login_progress_signal = pyqtSignal(int)
    login_success_signal = pyqtSignal(bool)
    search_progress_signal = pyqtSignal(int)
    content_signal = pyqtSignal(str)
    image_signal = pyqtSignal(str)
    def __init__(self):
        QObject.__init__(self, None)
        cp = chromedriver_autoinstaller.install()
        self.browser = webdriver.Chrome(cp)
        self.input_id = ""
        self.input_pw = ""
        self.keyword = ""

    def login(self):
        self.login_progress_signal.emit(10)
        self.browser.get("https://www.instagram.com/accounts/login/?hl=ko")
        self.login_progress_signal.emit(20)
        time.sleep(3)
        self.login_progress_signal.emit(30)
        id = self.browser.find_element_by_name("username")
        self.login_progress_signal.emit(40)
        id.send_keys(self.input_id)
        self.login_progress_signal.emit(50)
        pw = self.browser.find_element_by_name("password")
        self.login_progress_signal.emit(60)
        pw.send_keys(self.input_pw)
        self.login_progress_signal.emit(70)
        self.browser.find_element_by_css_selector("div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB").click()
        self.login_progress_signal.emit(90)
        time.sleep(4)
        self.login_progress_signal.emit(100)
        if self.browser.current_url == "https://www.instagram.com/accounts/login/?hl=ko":
            self.login_success_signal.emit(False)
        else:
            self.login_success_signal.emit(True)

    def search(self):
        self.search_progress_signal.emit(20)
        url = "https://www.instagram.com/explore/tags/{}/?hl=ko".format(self.keyword)
        self.search_progress_signal.emit(40)
        self.browser.get(url)
        self.search_progress_signal.emit(60)
        time.sleep(4)
        self.search_progress_signal.emit(80)
        # ????????? ?????? ??????
        self.browser.find_element_by_css_selector("div._9AhH0").click()
        self.search_progress_signal.emit(90)
        time.sleep(5)
        self.search_progress_signal.emit(100)
        # ?????? ????????? ??????.
        while True:
            like = self.browser.find_element_by_css_selector("button.wpO6b span > svg._8-yf5")
            value = like.get_attribute("aria-label")
            next = self.browser.find_element_by_css_selector("a._65Bje.coreSpriteRightPaginationArrow")
            ### ????????? ###
            nick_name = self.browser.find_element_by_css_selector("a.sqdOP.yWX7d._8A5w5.ZIAjV")
            content = self.browser.find_element_by_css_selector("div.C4VMK > span")
            self.content_signal.emit(content.text)
            try:
                img = self.browser.find_element_by_css_selector("article.M9sTE.L_LMM.JyscU.ePUX4 div.KL4Bh > img")
                img_url = img.get_attribute("src")
            except: # ???????????? ????????????????
                img = self.browser.find_element_by_css_selector("video.tWeCl")
                img_url = img.get_attribute("poster")

            self.image_signal.emit(img_url)

            if value == "?????????":  # ???????????? ???????????????????
                like.click()
                time.sleep(random.randint(2, 5) + random.random())
                next.click()
                time.sleep(random.randint(2, 5) + random.random())
            elif value == "????????? ??????":  # ???????????? ????????????????
                next.click()
                time.sleep(random.randint(2, 5) + random.random())

class MainDialog(QDialog):
    login_signal = pyqtSignal()
    search_signal = pyqtSignal()
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(ui_file, self)
        self.login_progressbar.setValue(0)
        self.search_progressbar.setValue(0)
        self.button_search.setEnabled(False)
        ###
        self.worker = SeleniumWorker()
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.thread.start()
        ####
        self.button_login.clicked.connect(self.LoginButtonClicked)
        self.login_signal.connect(self.worker.login)
        self.worker.login_progress_signal.connect(self.login_progressbar.setValue)
        self.worker.login_success_signal.connect(self.finish_login)
        self.button_search.clicked.connect(self.SearchButtonClicked)
        self.search_signal.connect(self.worker.search)
        self.worker.search_progress_signal.connect(self.loading_search)
        self.worker.image_signal.connect(self.show_image)
        self.worker.content_signal.connect(self.show_content)

    def show_image(self, data):
        img = req.urlopen(data).read()
        pixmap = QPixmap()
        pixmap.loadFromData(img)
        pixmap = pixmap.scaled(250, 250)
        self.img_label.setPixmap(pixmap)

    def show_content(self, data):
        self.text_label.clear()
        self.text_label.append(data)

    def loading_search(self, data):
        self.search_progressbar.setValue(data)
        if data == 100:
            self.search_status.setText("?????? ??????! ?????? ????????? ????????? ???....")

    def SearchButtonClicked(self):
        self.search_status.setText("?????? ??? .....")
        self.worker.keyword = self.input_search.text()
        self.search_signal.emit()

    def finish_login(self, data):
        if data == True:
            self.login_status.setText("????????? ??????!")
            self.button_search.setEnabled(True)
        else:
            self.login_status.setText("????????? ??????! ?????? ??????????????????..")
            self.button_login.setEnabled(True)

    def LoginButtonClicked(self):
        self.button_login.setEnabled(False)
        user_id = self.input_id.text()
        user_pw = self.input_pw.text()
        self.worker.input_id = user_id
        self.worker.input_pw = user_pw
        self.login_signal.emit()





QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())