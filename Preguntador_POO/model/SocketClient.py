import socket

class SocketClient:
    def __init__(self, host="172.17.0.2", port=8587):  # ip del servidor
        self.host = host
        self.port = port

    def send_request(self, message):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
        sock.sendall(message.encode())
        data = sock.recv(1024).decode()
        sock.close()
        return data
