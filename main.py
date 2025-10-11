import sys
from PySide6.QtWidgets import QApplication, QDialog
from ui import Ui_Dialog

class RoyalRoadDownloader(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        
        # Now setupUi will work because we inherit from both QDialog and Ui_Dialog
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = RoyalRoadDownloader()
    window.show()
    
    sys.exit(app.exec())