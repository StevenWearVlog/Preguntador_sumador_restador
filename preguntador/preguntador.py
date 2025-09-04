import socket

SUMADOR_IP = "172.17.0.4"  # nombre del contenedor
SUMADOR_PORT = 5000

def main():
    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))
    c = int(input("Ingrese c: "))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SUMADOR_IP, SUMADOR_PORT))

    sock.send(f"{a},{b},{c}".encode("utf-8"))
    respuesta = sock.recv(1024).decode("utf-8")
    print("Respuesta del sistema:", respuesta)
    sock.close()

if __name__ == "__main__":
    main()
