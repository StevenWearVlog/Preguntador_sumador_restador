import socket

# Configuración
HOST = "172.17.0.4"
PORT = 5000
RESTADOR_IP = "172.17.0.3"   # nombre del contenedor
RESTADOR_PORT = 5001

def handle_client(conn):
    data = conn.recv(1024).decode("utf-8")
    if not data:
        return

    # Datos recibidos desde preguntador
    try:
        a, b, c = map(int, data.split(","))
    except:
        conn.send("Error: formato debe ser a,b,c".encode("utf-8"))
        return

    # Conectar con restador
    restador_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    restador_sock.connect((RESTADOR_IP, RESTADOR_PORT))
    restador_sock.send(f"{b},{c}".encode("utf-8"))

    # Respuesta del restador
    result_rest = int(restador_sock.recv(1024).decode("utf-8"))
    restador_sock.close()

    # Hacer la suma
    total = a + result_rest
    conn.send(f"R = {a} + ({b} - {c}) = {total}".encode("utf-8"))

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(5)
        print("Sumador esperando en puerto", PORT)

        while True:
            conn, _ = server.accept()
            handle_client(conn)
            conn.close()

if __name__ == "__main__":
    main()
