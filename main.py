import sys
from PySide6.QtWidgets import QApplication, QDialog
from ui import Ui_Dialog
from downloader import Downloader

class RoyalRoadDownloader(QDialog, Ui_Dialog):
    def __init__(self):
        #Init base class
        super().__init__()
        self.setupUi(self)
        

        self.progressBar.setValue(0)
        self.urlLine.setText("https://www.royalroad.com/fiction/51893/the-heart-grows")

        self.rr_light_button.clicked.connect(self.rr_light_bttn)
        self.rr_dark_button.clicked.connect(self.rr_dark_bttn)
        self.midnight_button.clicked.connect(self.midnight_bttn)
        self.antique_button.clicked.connect(self.antique_bttn)

        self.txt_button.clicked.connect(self.txt_bttn)
        self.html_button.clicked.connect(self.html_bttn)
        self.pdf_button.clicked.connect(self.pdf_bttn)

        self.downloader = Downloader()

    def _switch_button(self, button):
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
        pass

    def txt_bttn(self):
        self._download_bttn()

    def html_bttn(self):
        self._download_bttn()

    def pdf_bttn(self):
        self._download_bttn()



app = QApplication(sys.argv)

window = RoyalRoadDownloader()
window.show()

sys.exit(app.exec())