import sys
from PySide6.QtWidgets import QApplication, QDialog
from ui import Ui_Dialog
from downloader import Downloader

class RoyalRoadDownloader(QDialog, Ui_Dialog):
    def __init__(self):
        #Init base class
        super().__init__()
        self.setupUi(self)     
        self.txt_button.setEnabled(False)
        self.html_button.setEnabled(False)
        self.pdf_button.setEnabled(False)        
        

        self.progressBar.setValue(0)
        self.urlLine.setText("https://www.royalroad.com/fiction/51893/the-heart-grows")
        self.urlLine.setText("https://www.royalroad.com/fiction/134167/sector-bomb")

        self.rr_light_button.clicked.connect(self.rr_light_bttn)
        self.rr_dark_button.clicked.connect(self.rr_dark_bttn)
        self.midnight_button.clicked.connect(self.midnight_bttn)
        self.antique_button.clicked.connect(self.antique_bttn)

        self.txt_button.clicked.connect(self.txt_bttn)
        self.html_button.clicked.connect(self.html_bttn)
        self.pdf_button.clicked.connect(self.pdf_bttn)

        self.downloader = Downloader()

    def _switch_button(self, button):
        #Enabling download buttons
        self.txt_button.setEnabled(True)
        self.html_button.setEnabled(True)
        self.pdf_button.setEnabled(True)     

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
        self.downloader.set_url(self.urlLine.text())
        self.downloader.get_url_list()
        self.downloader.download()

    def txt_bttn(self):
        self._download_bttn()
        self.downloader.to_txt()

    def html_bttn(self):
        self._download_bttn()

        if self.rr_light_button.property("selected") == True:
            self.downloader.to_html("templates/html/light.html")
        elif self.rr_dark_button.property("selected") == True:
            self.downloader.to_html("templates/html/dark.html")
        elif self.midnight_button.property("selected") == True:
            self.downloader.to_html("templates/html/midnight.html")
        elif self.antique_button.property("selected") == True:
            self.downloader.to_html("templates/html/antique.html")


    def pdf_bttn(self):
        self._download_bttn()

        if self.rr_light_button.property("selected") == True:
            self.downloader.to_pdf("templates/pdf/light.html")
        elif self.rr_dark_button.property("selected") == True:
            self.downloader.to_pdf("templates/pdf/dark.html")
        elif self.midnight_button.property("selected") == True:
            self.downloader.to_pdf("templates/pdf/midnight.html")
        elif self.antique_button.property("selected") == True:
            self.downloader.to_pdf("templates/pdf/antique.html")

app = QApplication(sys.argv)

window = RoyalRoadDownloader()
window.show()

sys.exit(app.exec())