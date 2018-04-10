# pyuic5 name.ui -o name.py
import sys
sys.path.append('forms')
sys.path.append('libs')
from MainFunctions import *

# Импортируем наш интерфейс из файла
from MainForm import *
from Classes import *  
from PyQt5 import QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow() # Сетапим макет
        self.ui.setupUi(self)
        # Сетап диалоговые окона
        self.dA = DAbout()
        self.dSP = DSavePath()
        self.settings = tabSettings()

        self.th = ConvTh(self)
        self.ath = ConvThA(self)
        
        # Преднастройка формы
        self.ui.progressBar.hide()
        self.ui.pushButton.setEnabled(False)

        # Vars
        self.currentFileName = '' # Текущий путь к файлу
        self.savePath = '' # Путь сохранения
        self.doneFile = '' # Название обработанного файла   
        self.preFile = '' # Название чистого файла
        self.formatFile = '' # Формать файла

        # Events
        # ===================================================
        # Button
        self.ui.pushButton.clicked.connect(lambda: convert(self)) # Слушатель на кнопку

        # MenuBar
        self.ui.actionOpen_file.triggered.connect(lambda: open_file(self)) # Слушатели на MenuBar
        self.ui.actionChange_save_path.triggered.connect(lambda: ChangeSavePath(self))
        self.ui.actionAbout.triggered.connect(lambda: About(self))
        self.ui.actionSettings.triggered.connect(lambda: SettingsStart(self))

        # Thread
        self.th.StatusBarSignal.connect(self.TextPBChange)
        self.th.ProgressBarSignal.connect(self.PBValueChange)
        self.th.finished.connect(lambda: FinishTh(self))

        # Слушатели на диалоговых окнах
        self.dSP.ui.pushButton.clicked.connect(lambda: ConfirmChoice(self))
        self.dSP.ui.toolButton.clicked.connect(lambda: ChangePath(self))
        self.settings.ui.pushButton.clicked.connect(lambda: ConfirmSettings(self))
        self.settings.ui.pushButton_2.clicked.connect(lambda: ConfirmSettings(self))
        self.settings.ui.aRBf_1.toggled.connect(lambda: EnabledSpinBox(self))

    # Thread functions
    def TextPBChange(self, s):
        self.ui.statusbar.showMessage(s)
        time.sleep(0.5)
        if s == 'Converting...':
            self.ui.progressBar.show()
        if s == 'Final touches':
            self.ui.progressBar.hide()
            self.ui.progressBar.setValue(0)

    def PBValueChange(self, i):
        self.ui.progressBar.setValue(i)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())