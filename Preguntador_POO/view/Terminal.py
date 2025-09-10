class TerminalView:
    @staticmethod
    def get_numbers():
        a = int(input("Ingrese a: "))
        b = int(input("Ingrese b: "))
        return a, b

    @staticmethod
    def show_result(result):
        print(f"Resultado recibido: {result}")
