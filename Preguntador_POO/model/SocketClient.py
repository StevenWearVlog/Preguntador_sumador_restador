import socket

class SocketClient:
    def __init__(self, host="172.17.0.3", port=8585):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.sock.connect((self.host, self.port))

    def send_data(self, data: str):
        self.sock.sendall(data.encode())

    def receive_data(self) -> str:
        return self.sock.recv(1024).decode()

    def close(self):
        self.sock.close()
