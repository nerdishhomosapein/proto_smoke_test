import socket
import threading


def handle_client(client_socket, address):
    request = client_socket.recv(1024)
    client_socket.send(request)
    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8080))
    server.listen(5)
    print("listening on port 8080")
    while True:
        client, address = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client, address))
        client_handler.start()


if __name__ == "__main__":
    start_server()
