from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QPushButton)
import collections
import client


class Graphics(QWidget):
    def __init__(self):
        super().__init__()
        title = 'SMTP'
        width = 600
        height = 600
        self.setWindowTitle(title)
        self.setMinimumSize(width, height)
        self.setMaximumSize(width, height)
        self.frames = {}
        self.mail_frame = None
        self.send_button = None
        self.set_widgets()

        self.client = client.Client()

    def set_widgets(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        frames = [('Server', QLineEdit()),
                  ('Port', QLineEdit()),
                  ('Login', QLineEdit()),
                  ('Password', QLineEdit()),
                  ('Receiver', QLineEdit())]

        self.frames = collections.OrderedDict(frames)
        for i, name in enumerate(self.frames.keys()):
            grid.addWidget(QLabel(name), i, 0)
            grid.addWidget(self.frames[name], i, 1)

        self.mail_frame = QTextEdit()
        self.send_button = QPushButton('Send', self)
        self.send_button.clicked.connect(self.send)
        grid.addWidget(QLabel('Mail:'), 6, 0)
        grid.addWidget(self.mail_frame, 6, 1)
        grid.addWidget(self.send_button, 11, 1)
        self.setLayout(grid)

    def send(self):
        server = self.frames['Server'].text()
        port = int(self.frames['Port'].text())

        self.client.connect(server, port)
        self.client.greeting()

        login = self.frames['Login'].text()
        password = self.frames['Password'].text()

        self.client.login(login, password)

        receiver = self.frames['Receiver'].text()

        self.client.set_sender(login)
        self.client.set_receiver(receiver)

        mail = self.mail_frame.toPlainText()

        self.client.send(mail)