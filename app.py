import sys

from PySide6 import QtWidgets
from bp_gui_widget import BpGuiMainWindow

app = QtWidgets.QApplication(sys.argv)

window = BpGuiMainWindow(app)
window.show()

app.exec()