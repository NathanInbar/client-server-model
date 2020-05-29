import socket, threading

SERVER = "192.168.86.30"#.174 lappy / .30 deskky
PORT = 5050
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def recieve():
    msg = client.recv(32).decode(FORMAT)
    print(msg)
def send(msg):
    client.send(msg.encode(FORMAT))

def update():
    while True:
        send("Client says hello")
        recieve()

def start():
    client.connect(ADDR)
    thread = threading.Thread(target=update)
    thread.start()
    run = True

start()
