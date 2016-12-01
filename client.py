import socket
import ssl
import base64


class Client:
    def __init__(self):
        self.server = None
        temp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket = ssl.wrap_socket(temp)
        self.address = None
        self.sender = None
        self.receiver = None

    def connect(self, server, port):
        if (server, port) == self.address:
    	    return
        self.socket.connect((server, port))
        self.address = (server, port)

    def greeting(self):
        self.socket.send('EHLO Test\r\n'.encode())
        self.socket.recv(1024).decode()

    def login(self, login, password):
        self.socket.sendall('AUTH LOGIN\r\n'.encode())
        self.socket.recv(1024).decode()

        self.socket.sendall(base64.b64encode(login.encode('ascii')))
        self.socket.sendall('\r\n'.encode())
        self.socket.recv(1024).decode()

        self.socket.sendall(base64.b64encode(password.encode('ascii')))
        self.socket.sendall('\r\n'.encode())
        self.socket.recv(1024).decode()

    def set_sender(self, email):
        self.socket.sendall('MAIL FROM: {0}\r\n'.format(email).encode())
        self.socket.recv(1024).decode()

    def set_receiver(self, email):
        self.socket.sendall('RCPT TO: {0}\r\n'.format(email).encode())
        self.socket.recv(1024).decode()

    def send(self, text):
        self.socket.sendall('DATA\r\n'.encode())
        self.socket.recv(1024).decode()

        self.socket.sendall('\r\n{0}\r\n.\r\n'.format(text).encode())
        self.socket.recv(1024).decode()