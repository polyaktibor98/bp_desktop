# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bp_gui_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QToolBar, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon = QIcon()
        icon.addFile(u":/images/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon)
        self.actionAboutQt = QAction(MainWindow)
        self.actionAboutQt.setObjectName(u"actionAboutQt")
        icon1 = QIcon()
        icon1.addFile(u":/images/aboutQt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAboutQt.setIcon(icon1)
        self.actionBrowse = QAction(MainWindow)
        self.actionBrowse.setObjectName(u"actionBrowse")
        icon2 = QIcon()
        icon2.addFile(u":/images/browse.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionBrowse.setIcon(icon2)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon3 = QIcon()
        icon3.addFile(u":/images/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon4 = QIcon()
        icon4.addFile(u":/images/quit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionQuit.setIcon(icon4)
        self.actionGenerate = QAction(MainWindow)
        self.actionGenerate.setObjectName(u"actionGenerate")
        icon5 = QIcon()
        icon5.addFile(u":/images/generate.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionGenerate.setIcon(icon5)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.browse_button = QPushButton(self.centralwidget)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setIcon(icon2)

        self.horizontalLayout.addWidget(self.browse_button)

        self.generate_button = QPushButton(self.centralwidget)
        self.generate_button.setObjectName(u"generate_button")
        self.generate_button.setIcon(icon5)

        self.horizontalLayout.addWidget(self.generate_button)

        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setIcon(icon3)

        self.horizontalLayout.addWidget(self.save_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.chart_view = QChartView(self.centralwidget)
        self.chart_view.setObjectName(u"chart_view")

        self.verticalLayout.addWidget(self.chart_view)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionBrowse)
        self.menuFile.addAction(self.actionGenerate)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)
        self.toolBar.addAction(self.actionBrowse)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionGenerate)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSave)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionAboutQt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.actionBrowse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionGenerate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.generate_button.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

