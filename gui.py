import sys
from PySide6 import QtCore, QtWidgets, QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Scape Video Downloader")
        self.setWindowIcon(QtGui.QIcon("eyeye.ico"))
        mainWidget = QtWidgets.QWidget()
        mainLayout = QtWidgets.QVBoxLayout(mainWidget)
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)
        
        
        self.fileTypeCombo = QtWidgets.QComboBox()
        self.fileTypeCombo.addItems(["mp4", "avi", "mov", "mkv"])
        self.resolutionCombo = QtWidgets.QComboBox()
        self.resolutionCombo.addItems(["144p", "240p", "360p", "480p", "720p", "1080p", "1440p"])
        
        self.desc = QtWidgets.QLabel("Enter a YouTube link and your desired extention and resolution.");
        self.linkBox = QtWidgets.QLineEdit()
    
    
        
        self.submitButton = QtWidgets.QPushButton("Download")
        
        mainLayout.addWidget(self.desc)
        drops = QtWidgets.QHBoxLayout()
        drops.addWidget(self.fileTypeCombo)
        drops.addWidget(self.resolutionCombo)
        mainLayout.addLayout(drops)
        mainLayout.addWidget(self.linkBox)
        mainLayout.addWidget(self.submitButton)
            


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    window = MainWindow()
    window.resize(800, 300)
    window.show()
    
    sys.exit(app.exec())