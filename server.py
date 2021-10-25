import socket   
import threading


host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
server.listen()
print(f"Servidor corriendo en {host}:{port}")


clients = []
usernames = []

def broadcast(message, _client):
    for client in clients:
        if client != _client:
            client.send(message)


def disconnected_client(client):
    index = clients.index(client)
    username = usernames[index]
    broadcast(f"Chat: {username} desconectado".encode('utf-8'), client)
    clients.remove(client)
    usernames.remove(username)
    client.close()
    print(f"{username} desconectado")


def handle_messages(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            disconnected_client(client)
            break


def receive_connections():
    while True:
        client, address = server.accept()

        
        username = client.recv(1024).decode('utf-8')

        clients.append(client)
        usernames.append(username)

        print(f"{username} conectado desde {str(address)}")

        message = f"Chat: {username} entro al chat!".encode("utf-8")
        broadcast(message, client)
        client.send("En linea".encode("utf-8"))

        thread = threading.Thread(target=handle_messages, args=(client,))
        thread.start()


receive_connections()