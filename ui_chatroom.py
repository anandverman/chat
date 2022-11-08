# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chatroom.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        iconThemeName = u"utilities-terminal"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../../.designer/backup", QSize(), QIcon.Normal, QIcon.Off)
        
        MainWindow.setWindowIcon(icon)
        self.actionMenu_Label = QAction(MainWindow)
        self.actionMenu_Label.setObjectName(u"actionMenu_Label")
        self.actionMenu_Label_2 = QAction(MainWindow)
        self.actionMenu_Label_2.setObjectName(u"actionMenu_Label_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout_6 = QGridLayout(self.page_1)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.chatroom_label = QLabel(self.page_1)
        self.chatroom_label.setObjectName(u"chatroom_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.chatroom_label.sizePolicy().hasHeightForWidth())
        self.chatroom_label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Kinnari"])
        font.setPointSize(32)
        font.setBold(True)
        self.chatroom_label.setFont(font)
        self.chatroom_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.chatroom_label, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, -1, 5, -1)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.name_edit = QLineEdit(self.page_1)
        self.name_edit.setObjectName(u"name_edit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.name_edit.sizePolicy().hasHeightForWidth())
        self.name_edit.setSizePolicy(sizePolicy2)
        self.name_edit.setMinimumSize(QSize(260, 0))
        self.name_edit.setMaximumSize(QSize(260, 16777215))
        self.name_edit.setInputMask(u"")

        self.gridLayout_7.addWidget(self.name_edit, 0, 1, 1, 1)

        self.name_label = QLabel(self.page_1)
        self.name_label.setObjectName(u"name_label")

        self.gridLayout_7.addWidget(self.name_label, 0, 0, 1, 1)

        self.serveraddr_edit = QLineEdit(self.page_1)
        self.serveraddr_edit.setObjectName(u"serveraddr_edit")
        sizePolicy2.setHeightForWidth(self.serveraddr_edit.sizePolicy().hasHeightForWidth())
        self.serveraddr_edit.setSizePolicy(sizePolicy2)
        self.serveraddr_edit.setMinimumSize(QSize(260, 0))
        self.serveraddr_edit.setMaximumSize(QSize(260, 16777215))

        self.gridLayout_7.addWidget(self.serveraddr_edit, 1, 1, 1, 1)

        self.serveraddr_label = QLabel(self.page_1)
        self.serveraddr_label.setObjectName(u"serveraddr_label")

        self.gridLayout_7.addWidget(self.serveraddr_label, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_7, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 7, -1, 60)
        self.submit_button = QPushButton(self.page_1)
        self.submit_button.setObjectName(u"submit_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.submit_button.sizePolicy().hasHeightForWidth())
        self.submit_button.setSizePolicy(sizePolicy3)

        self.gridLayout_4.addWidget(self.submit_button, 0, 0, 1, 1)

        self.result_edit = QLabel(self.page_1)
        self.result_edit.setObjectName(u"result_edit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.result_edit.sizePolicy().hasHeightForWidth())
        self.result_edit.setSizePolicy(sizePolicy4)
        self.result_edit.setMinimumSize(QSize(0, 50))
        self.result_edit.setScaledContents(False)
        self.result_edit.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.result_edit, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout_6.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_9 = QGridLayout(self.page_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.username_label = QLabel(self.page_2)
        self.username_label.setObjectName(u"username_label")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.username_label.setFont(font1)
        self.username_label.setFrameShape(QFrame.Box)
        self.username_label.setFrameShadow(QFrame.Raised)
        self.username_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.username_label, 0, 1, 1, 2)

        self.back_button = QPushButton(self.page_2)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setMaximumSize(QSize(25, 16777215))
        font2 = QFont()
        font2.setFamilies([u"codicon"])
        self.back_button.setFont(font2)
        icon1 = QIcon()
        iconThemeName = u"go-previous"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.back_button.setIcon(icon1)

        self.gridLayout_8.addWidget(self.back_button, 0, 0, 1, 1)

        self.typemessage_edit = QLineEdit(self.page_2)
        self.typemessage_edit.setObjectName(u"typemessage_edit")

        self.gridLayout_8.addWidget(self.typemessage_edit, 2, 0, 1, 2)

        self.send_button = QPushButton(self.page_2)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_8.addWidget(self.send_button, 2, 2, 1, 1)

        self.scrollArea = QScrollArea(self.page_2)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy5)
        self.scrollArea.setFrameShape(QFrame.Box)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 741, 539))
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_8.addWidget(self.scrollArea, 1, 0, 1, 3)


        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Chat Room", None))
        self.actionMenu_Label.setText(QCoreApplication.translate("MainWindow", u"Menu Label", None))
        self.actionMenu_Label_2.setText(QCoreApplication.translate("MainWindow", u"Menu Label", None))
        self.chatroom_label.setText(QCoreApplication.translate("MainWindow", u"CHAT ROOM", None))
        self.name_edit.setText("")
        self.name_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter name here", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"Enter your Name", None))
        self.serveraddr_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"eg. 192.168.29.102:2202", None))
        self.serveraddr_label.setText(QCoreApplication.translate("MainWindow", u"Enter Server Address", None))
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.result_edit.setText(QCoreApplication.translate("MainWindow", u"....", None))
        self.username_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.typemessage_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type Message Here", None))
        self.send_button.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi

