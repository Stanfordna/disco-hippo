#! ../../../.venv/Scripts/python
"""
    Leeloo listens for requests and probably in the future will make them available for a request visualizer
"""
import socket
import ssl
import subprocess

def get_local_ip():
    # TODO: move into separate module
    # Define the piped commands
    cmd1 = ["ipconfig"]
    cmd2 = ["grep", "IPv4"]
    cmd3 = ["grep", "-o", "[0-9.]*$"]

    # Create the subprocesses
    p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(cmd2, stdin=p1.stdout, stdout=subprocess.PIPE)
    p3 = subprocess.Popen(cmd3, stdin=p2.stdout, stdout=subprocess.PIPE)

    # Close the unused file descriptors
    p1.stdout.close()
    p2.stdout.close()

    # Get the output
    ip, _ = p3.communicate()
    p3.stdout.close()
    return ip.decode().strip()

def listen() -> None:
    """ Listens for requests """
    # TODO: Learn about socket address families and SocketKind
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # TODO: Understand bind address and possibly use local/internal ip from get_local_ip()
    _socket.bind(('0.0.0.0', 443))
    _socket.listen(5)
    # TODO: learn about other protocols 
    _sslContext = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    while True:
        # Accept a new connection
        conn, addr = _socket.accept()
        # data = _socket.recv(1024)
        print(f"Received curl request")

        # Send a response to the client
        _socket.sendall(b"Hello from the server!")
        # Wrap the connection with SSL
        # with _sslContext.wrap_socket(conn, server_side=True) as _socket:
        #     # Receive data from the client
        #     data = _socket.recv(1024)
        #     print(f"Received: {data.decode()}")

        #     # Send a response to the client
        #     _socket.sendall(b"Hello from the server!")

def examine() -> None:
    """ Examines Requests """

def forward() -> None:
    """ Forwards Requests """
