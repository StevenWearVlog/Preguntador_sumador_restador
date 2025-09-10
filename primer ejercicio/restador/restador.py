import socket

HOST = "172.17.0.3"
PORT = 5001

def handle_client(conn):
    data = conn.recv(1024).decode("utf-8")
    if not data:
        return
    try:
        b, c = map(int, data.split(","))
        result = b - c
        print (result)
        conn.send(str(result).encode("utf-8"))
    except:
        conn.send("Error en restador".encode("utf-8"))

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(5)
        print("Restador esperando en puerto", PORT)

        while True:
            conn, _ = server.accept()
            handle_client(conn)
            conn.close()

if __name__ == "__main__":
    main()
