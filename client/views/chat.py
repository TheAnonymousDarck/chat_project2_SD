# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ChatForm(object):
    def setupUi(self, chatForm):
        if not chatForm.objectName():
            chatForm.setObjectName(u"chatForm")
        chatForm.resize(877, 538)
        self.frame = QFrame(chatForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 877, 91))
        self.frame.setStyleSheet(u"background-color:#14258b")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 30, 241, 31))
        self.label.setStyleSheet(u"color: white;")
        self.logoutButton = QPushButton(self.frame)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setGeometry(QRect(750, 0, 81, 61))
        self.logoutButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.logoutButton.setStyleSheet(u"QPushButton:hover\n"
"    {\n"
"        border-style: solid;\n"
"        background-color:#bbdefb;\n"
"\n"
"    }\n"
"\n"
"    QPushButton:pressed\n"
"    {\n"
"            background-color:#0069c0;\n"
"    }")
        icon = QIcon()
        icon.addFile(u"client/assets/icons8-exit-200.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutButton.setIcon(icon)
        self.logoutButton.setIconSize(QSize(60, 60))
        self.logoutButton.setFlat(True)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(760, 60, 61, 16))
        self.label_2.setStyleSheet(u"color: white;")
        self.chatTextEdit = QTextEdit(chatForm)
        self.chatTextEdit.setObjectName(u"chatTextEdit")
        self.chatTextEdit.setGeometry(QRect(0, 90, 877, 381))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.chatTextEdit.setFont(font)
        self.chatTextEdit.setStyleSheet(u"background-color:#719fe4; \n"
"color: white")
        self.chatTextEdit.setReadOnly(True)
        self.frame_2 = QFrame(chatForm)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 470, 877, 71))
        self.frame_2.setStyleSheet(u"background-color: white")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.messageLineEdit = QLineEdit(self.frame_2)
        self.messageLineEdit.setObjectName(u"messageLineEdit")
        self.messageLineEdit.setGeometry(QRect(20, 10, 701, 41))
        font1 = QFont()
        font1.setPointSize(10)
        self.messageLineEdit.setFont(font1)
        self.sendButton = QPushButton(self.frame_2)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setGeometry(QRect(800, 10, 71, 51))
        self.sendButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.sendButton.setStyleSheet(u"QPushButton:hover\n"
"    {\n"
"        border-style: solid;\n"
"        background-color:#bbdefb;\n"
"\n"
"    }\n"
"\n"
"    QPushButton:pressed\n"
"    {\n"
"            background-color:#0069c0;\n"
"    }")
        icon1 = QIcon()
        icon1.addFile(u"client/assets/icons8-email-send-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sendButton.setIcon(icon1)
        self.sendButton.setIconSize(QSize(60, 60))
        self.sendButton.setFlat(True)
        self.sendImgButton = QPushButton(self.frame_2)
        self.sendImgButton.setObjectName(u"sendImgButton")
        self.sendImgButton.setGeometry(QRect(727, 10, 71, 51))
        self.sendImgButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.sendImgButton.setStyleSheet(u"QPushButton:hover\n"
"    {\n"
"        border-style: solid;\n"
"        background-color:#bbdefb;\n"
"\n"
"    }\n"
"\n"
"    QPushButton:pressed\n"
"    {\n"
"            background-color:#0069c0;\n"
"    }")
        icon2 = QIcon()
        icon2.addFile(u"client/assets/icons8-archivo-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sendImgButton.setIcon(icon2)
        self.sendImgButton.setIconSize(QSize(60, 60))
        self.sendImgButton.setFlat(True)

        self.retranslateUi(chatForm)

        QMetaObject.connectSlotsByName(chatForm)
    # setupUi

    def retranslateUi(self, chatForm):
        chatForm.setWindowTitle(QCoreApplication.translate("chatForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("chatForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">CHAT</span></p></body></html>", None))
        self.logoutButton.setText("")
        self.label_2.setText(QCoreApplication.translate("chatForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">SALIR</span></p></body></html>", None))
        self.messageLineEdit.setPlaceholderText(QCoreApplication.translate("chatForm", u"Type Something to send...", None))
        self.sendButton.setText("")
        self.sendImgButton.setText("")
    # retranslateUi

