from model.SocketClient import SocketClient
from view.Terminal import Terminal

class Controller:
    def __init__(self):
        self.model = SocketClient()
        self.view = Terminal()

    def run(self):
        while True:
            a = int(input("Ingrese a (0 para salir): "))
            if a == 0:
                print("Saliendo del cliente...")
                break

            b = int(input("Ingrese b: "))
            result = self.model.send_request(f"{a},{b}")
            self.view.show_result(result)
