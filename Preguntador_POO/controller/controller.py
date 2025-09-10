from model.SocketClient import SocketModel
from view.Terminal import TerminalView

class Controller:
    def __init__(self):
        self.model = SocketModel()
        self.view = TerminalView()

    def run(self):
        a, b = self.view.get_numbers()
        self.model.connect()
        self.model.send_data(f"{a},{b}")
        result = self.model.receive_data()
        self.view.show_result(result)
        self.model.close()
