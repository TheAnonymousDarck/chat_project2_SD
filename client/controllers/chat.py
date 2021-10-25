from PySide2 import QtCore
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QLabel, QWidget, QFileDialog
from PySide2.QtCore import Qt

from views.chat import ChatForm
from controllers.login import LoginWindow

import socket
import threading
import shutil
import time
import os.path


class ChatWindow(QWidget, ChatForm):

    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setupUi(self)

        self.connect()

        self.sendButton.clicked.connect(self.send_messages)
        self.sendImgButton.clicked.connect(self.send_images)


    def connect(self):
        connection_data = ('127.0.0.1', 55555)
        af_inet = socket.AF_INET
        sock_stream = socket.SOCK_STREAM

        self.client = socket.socket(af_inet, sock_stream)
        self.client.connect(connection_data)

        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.daemon = True
        receive_thread.start()

        self.client.send(self.username.encode('utf-8'))
        self.logoutButton.clicked.connect(self.logout)
    

    def logout(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.client.close()
        self.close()


    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                self.chatTextEdit.append(message)
                self.chatTextEdit.setAlignment(Qt.AlignLeft)
            except:
                self.client.close()
                break
    

    def send_messages(self):
        message = self.messageLineEdit.text()

        message = f"{self.username}: {message}"
        self.client.send(message.encode('utf-8'))
        self.chatTextEdit.append(message)
        self.chatTextEdit.setAlignment(Qt.AlignRight)
        self.messageLineEdit.clear()


    def send_images(self):
        # capturamos el path del archivo
        file_path = QFileDialog.getOpenFileName()[0]
        # la ruta obtenida previamente, la pondremos en
        # nuestro campo de mensaje
        self.messageLineEdit.setText(file_path)

        # guardamos lo que tenga nuestro campo de mensaje 
        # (en este caso, la ruta del archivo)
        imgMessage = self.messageLineEdit.text()

        # le damos formato a nuestro archivo a copiar 
        # para eso haremos lo siguiente:
        #   obtenemos la extención del archivo
        name, ext = os.path.splitext(imgMessage)
        
        # obtenemos la fecha de cuando se envio
        timestr = time.strftime("%Y%m%d-%H%M%S")

        # concatenamos nuestros valores para que cada archivo enviado tenga un formato
        filename = self.username + "-sent-" + timestr + ext
        # asignamos una variable con la ruta donde se van a guardar los archivos
        new_path = "client/filesSent/" + filename

        shutil.copy2(imgMessage, new_path)        

        img = self.load_img(new_path)

        imgMessage = f"{self.username}: {img}"
        self.client.send(imgMessage.encode('utf-8'))
        self.chatTextEdit.append(imgMessage)
        self.chatTextEdit.setAlignment(Qt.AlignRight)
        self.messageLineEdit.clear()


    def load_img(self, path):
        # self.img = QPixmap(path).scaledToWidth(100)
        # self.setPixmap(self.img)

        label = QLabel(self)
        pixmap = QPixmap(path)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
