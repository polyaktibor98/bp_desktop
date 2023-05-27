from PySide6.QtWidgets import QMainWindow
from ui_bp_gui_widget import Ui_MainWindow


def kiir():
    print("szia")


class BpGuiMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Blood pressure app")
        kiir()
