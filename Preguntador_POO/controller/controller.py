from model.SocketClient import SocketClient
from view.Terminal import Terminal

class Controller:
    def __init__(self):
        self.model = SocketClient()
        self.view = Terminal()

    def run(self):
        a = int(input("Ingrese a: "))
        b = int(input("Ingrese b: "))

        self.model.connect()
        self.model.send_data(f"{a},{b}")

        result = self.model.receive_data()
        self.view.show_result(a, b, result)

        self.model.close()
