from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from ui_bp_gui_widget import Ui_MainWindow
import pandas as pd


class BpGuiMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.setWindowTitle("Blood pressure app")

        self.actionQuit.triggered.connect(self.quit_app)
        self.actionAbout.triggered.connect(self.about_app)
        self.actionAboutQt.triggered.connect(self.about_qt)
        self.actionBrowse.triggered.connect(self.browse_file)

        self.browse_button.clicked.connect(self.browse_file)

        self.dates = []
        self.systolic = []
        self.diastolic = []
        self.pulse = []

    def quit_app(self):
        self.app.quit()
    
    def about_app(self):
        QMessageBox.information(self, "About the app", "This application is designed to visualize blood pressure values.\n\nQt for Python (PySide6) was used.")
    
    def about_qt(self):
        self.app.aboutQt()
        print(self.valami)

    def browse_file(self):
        file = QFileDialog.getOpenFileName(self, "Open CSV file", "", "CSV files (*.csv)")
        file_path = file[0]
        self.open_file(file_path)
    
    def open_file(self, file_path):
        data = pd.read_csv(file_path, parse_dates=["date"],
                usecols=["date", "systolic", "diastolic", "pulse"])
        #print(data.to_string())
        self.dates = data["date"].tolist()
        self.systolic = data["systolic"].tolist()
        self.diastolic = data["diastolic"].tolist()
        self.pulse = data["pulse"].tolist()
        print(self.dates)
