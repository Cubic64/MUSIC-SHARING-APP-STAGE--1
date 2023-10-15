import socket
from threading import Thread

IP_ADDRESS = '127.0.0.1'
PORT = 8080
SERVER = None
BUFFER_SIZE = 4096
clients = {}

def setup():
    print("\n\t\t\t\t\t\tIP MESSENGER\n")

    global PORT
    global SERVER
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind({IP_ADDRESS,PORT})

    SERVER.listen(100)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...")
    print("\n")

    acceptConnections()

setup_thread = Thread(target=setup)
setup_thread.start()

def acceptConnections():
    global SERVER
    global clients

    while True:
        clients, addr = SERVER.accept()
        print(clients.addr)