import socket
import threading
from datetime import datetime

def handle_client(client_socket):
    with client_socket:
        while True:
            request = client_socket.recv(1024)
            if request:
                request_str = request.decode('utf-8')
                if request_str.startswith('TIME') and request_str.endswith('\r\n'):
                    current_time = datetime.now().strftime('%H:%M:%S')
                    response = f'JAM {current_time}\r\n'
                    client_socket.send(response.encode('utf-8'))
                elif request_str.startswith('QUIT') and request_str.endswith('\r\n'):
                    break
            else:
                break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 45000))
    server.listen(5)
    print('Server listening on port 45000')

    while True:
        client_socket, addr = server.accept()
        print(f'Accepted connection from {addr}')
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
