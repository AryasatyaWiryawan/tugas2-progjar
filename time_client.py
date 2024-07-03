import socket

def send_request(request):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 45000))
    client.send(request.encode('utf-8'))
    response = client.recv(1024)
    print('Received:', response.decode('utf-8'))
    client.close()

if __name__ == "__main__":
    send_request('TIME\r\n')
    send_request('QUIT\r\n')
