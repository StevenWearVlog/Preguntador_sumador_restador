import socket

class SocketModel:
    def __init__(self, host="0.0.0.0", port=8282):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_server(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen()
        print(f"Servidor escuchando en {self.host}:{self.port}")
        return self.sock.accept()

    def close(self):
        self.sock.close()
