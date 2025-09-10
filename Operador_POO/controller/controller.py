from model.SocketServer import SocketServer
from view.Terminal import Terminal

class Controller:
    def __init__(self):
        self.model = SocketServer()
        self.view = Terminal()

    def run(self):
        print("Servidor iniciado, esperando clientes...\n")
        while True:  # 🔁 solo aceptamos clientes, sin rebind
            conn, addr = self.model.accept_client()
            self.view.show_message(f"Conexión establecida desde {addr}")

            try:
                data = conn.recv(1024).decode()
                if not data:
                    continue

                a, b = map(int, data.split(","))
                result = a + b

                conn.sendall(str(result).encode())
                self.view.show_result(a, b, result)

            finally:
                conn.close()
