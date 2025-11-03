import sys, os
from threading import Thread
from PySide6.QtCore import QTimer, QObject, Signal
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from ui import Ui_Dialog
from downloader import Downloader


class NotificationSignal(QObject):
    notify_signal = Signal(str)
    finished_download = Signal()


class RoyalRoadDownloader(QDialog, Ui_Dialog):
    def __init__(self):
        #Init base class
        super().__init__()
        self.setupUi(self)     
        self.txt_button.setEnabled(False)
        self.html_button.setEnabled(False)
        self.pdf_button.setEnabled(False)        

        #Signal
        self.signal = NotificationSignal()
        self.signal.notify_signal.connect(self._notify)
        self.signal.finished_download.connect(self._download_finish)
        
        #Load bar update
        self.timer = QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.update_bar)

        #Setup
        self.progressBar.setValue(0)
        self.urlLine.setText("https://www.royalroad.com/fiction/51893/the-heart-grows")
        # self.urlLine.setText("https://www.royalroad.com/fiction/134167/sector-bomb")

        self.progressBar.setTextVisible(True)    #To make sure the label is drawn
        self.progressBar.setFormat("")

        self.rr_light_button.clicked.connect(self.rr_light_bttn)
        self.rr_dark_button.clicked.connect(self.rr_dark_bttn)
        self.midnight_button.clicked.connect(self.midnight_bttn)
        self.antique_button.clicked.connect(self.antique_bttn)

        self.txt_button.clicked.connect(self.txt_bttn)
        self.html_button.clicked.connect(self.html_bttn)
        self.pdf_button.clicked.connect(self.pdf_bttn)

        self.downloader = Downloader()

    def _notify(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Downloader")
        msg.setText(message)
        msg.setIcon(QMessageBox.Information)
        QApplication.beep()
        msg.exec()

    def _enable_download(self):
        self.txt_button.setEnabled(True)
        self.html_button.setEnabled(True)
        self.pdf_button.setEnabled(True)  

    def _disable_download(self):
        self.txt_button.setEnabled(False)
        self.html_button.setEnabled(False)
        self.pdf_button.setEnabled(False)  

    def _switch_button(self, button):
        #Enabling download buttons
        self._enable_download()

        #Switching buttons
        self.rr_light_button.setEnabled(True)
        self.rr_dark_button.setEnabled(True)
        self.midnight_button.setEnabled(True)
        self.antique_button.setEnabled(True)

        self.rr_light_button.setProperty("selected", False)
        self.rr_dark_button.setProperty("selected", False)
        self.midnight_button.setProperty("selected", False)
        self.antique_button.setProperty("selected", False)

        self.rr_light_button.style().polish(self.rr_light_button)
        self.rr_dark_button.style().polish(self.rr_dark_button)
        self.midnight_button.style().polish(self.midnight_button)
        self.antique_button.style().polish(self.antique_button)

        match button:
            case 1:
                self.rr_light_button.setProperty("selected", True)
                self.rr_light_button.style().polish(self.rr_light_button)
            case 2:
                self.rr_dark_button.setProperty("selected", True)
                self.rr_dark_button.style().polish(self.rr_dark_button)
            case 3:
                self.midnight_button.setProperty("selected", True)
                self.midnight_button.style().polish(self.midnight_button)
            case 4:
                self.antique_button.setProperty("selected", True)
                self.antique_button.style().polish(self.antique_button)

    def rr_light_bttn(self):
        self._switch_button(1)

    def rr_dark_bttn(self):
        self._switch_button(2)

    def midnight_bttn(self):
        self._switch_button(3)

    def antique_bttn(self):
        self._switch_button(4)


    def _download_bttn(self):
        self.downloader.redownload = self.delete_check.isChecked()
        self.downloader.update_cache = self.update_check.isChecked()

        self.downloader.set_url(self.urlLine.text())
        self.downloader.get_url_list()
        self.downloader.download()
    
    def _signal_finish(self):
        self.progressBar.setFormat("Done! - %p%")
        self.signal.finished_download.emit()
        self.signal.notify_signal.emit("Downloading finished!")

    def _download_finish(self):
        self._enable_download()
        self.progressBar.setValue(100)

    def _get_base_path(self):
        if hasattr(sys, '_MEIPASS'):              #Pyinstaller
            return sys._MEIPASS
        else:                                     #not Pyinstaller
            return os.path.abspath(".")

    def txt_bttn(self):
        self.timer.start(100)
        
        self._disable_download()

        def thread():
            self._download_bttn()
            self.downloader.to_txt()

            self._signal_finish()

        Thread(target=thread).start()

    def html_bttn(self):
        self.timer.start(100)

        self._disable_download()

        def thread():
            self._download_bttn()

            if self.rr_light_button.property("selected") == True:
                self.downloader.to_html(self._get_base_path() + "/templates/html/light.html")
            elif self.rr_dark_button.property("selected") == True:
                self.downloader.to_html(self._get_base_path() + "/templates/html/dark.html")
            elif self.midnight_button.property("selected") == True:
                self.downloader.to_html(self._get_base_path() + "/templates/html/midnight.html")
            elif self.antique_button.property("selected") == True:
                self.downloader.to_html(self._get_base_path() + "/templates/html/antique.html")

            self._signal_finish()

        Thread(target=thread).start()

    def pdf_bttn(self):
        self.timer.start(100)

        self._disable_download()

        def thread():
            self._download_bttn()

            self.progressBar.setFormat("Creating PDF... - %p%")

            if self.rr_light_button.property("selected") == True:
                self.downloader.to_pdf(self._get_base_path() + "/templates/pdf/light.html")
            elif self.rr_dark_button.property("selected") == True:
                self.downloader.to_pdf(self._get_base_path() + "/templates/pdf/dark.html")
            elif self.midnight_button.property("selected") == True:
                self.downloader.to_pdf(self._get_base_path() + "/templates/pdf/midnight.html")
            elif self.antique_button.property("selected") == True:
                self.downloader.to_pdf(self._get_base_path() + "/templates/pdf/antique.html")

            self._signal_finish()

        Thread(target=thread).start()


    def update_bar(self):
        if self.downloader.chap_downloaded != 0:
            if self.downloader.chap_num == self.downloader.chap_downloaded:
                self.timer.stop()
            else:
                self.progressBar.setFormat(f"Downloading {self.downloader.chap_downloaded}/{self.downloader.chap_num} - %p%")
                self.progressBar.setValue((self.downloader.chap_downloaded / self.downloader.chap_num) * 99)
        else:
            self.progressBar.setFormat("")
            self.progressBar.setValue(0)

#Debug
# import shutil
# shutil.rmtree("cache")

#Main
app = QApplication(sys.argv)

window = RoyalRoadDownloader()
window.show()

sys.exit(app.exec())