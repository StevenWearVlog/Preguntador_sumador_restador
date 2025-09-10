from model.socketServer import SocketServer
from view.Terminal import Terminal

class Controller:
    def __init__(self):
        self.model = SocketServer()
        self.view = Terminal()

    def run(self):
        conn, addr = self.model.start_server()
        self.view.show_message(f"Conexión establecida desde {addr}")

        data = conn.recv(1024).decode()
        a, b = map(int, data.split(","))
        result = a + b

        conn.sendall(str(result).encode())
        conn.close()

        self.view.show_result(a, b, result)
        self.model.close()
