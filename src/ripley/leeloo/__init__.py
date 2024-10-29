#! ../../../.venv/Scripts/python
"""
    Leeloo listens for requests and probably in the future will make them available for a request visualizer
"""
import socket
import ssl

def listen() -> None:
    """ Listens for requests """
    # TODO: Learn about socket address families and SocketKind
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # TODO: Understand bind address
    _socket.bind(('0.0.0.0', 443))
    _socket.listen(5)
    # TODO: learn about other protocols 
    _sslContext = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

def examine() -> None:
    """ Examines Requests """

def forward() -> None:
    """ Forwards Requests """
