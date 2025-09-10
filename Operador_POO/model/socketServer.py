import socket

class SocketServer:
    def __init__(self, host="0.0.0.0", port=8587):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 🔑 reusar puerto
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        print(f"Servidor escuchando en {self.host}:{self.port}")

    def accept_client(self):
        return self.sock.accept()


