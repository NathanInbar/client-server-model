import socket, threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []

def handle_client(conn,addr):
    print(f"[CONNECTION]{addr} has connected.")
    clients.append(conn)
    connected = True

    while connected:
        recieve(conn)
        send(conn,"Server says hello")

def recieve(conn):
    msg = conn.recv(32).decode(FORMAT)
    print(msg)

def send(conn,msg):
        conn.send(msg.encode(FORMAT))

def start():
    print("[STARTING] Server is starting...")
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()

start()
