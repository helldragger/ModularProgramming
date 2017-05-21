"""
Communicate from the client to the server
"""

import socket as socket


server = 'localhost'
port = 22222


def on_init():
    """
    Initialize the tcp server and returns the socket
    :return: the tcp socket
    """
    # Opens a socket
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Binds the socket
    tcpsock.bind(("", port))
    return tcpsock


def ask_database(request):
    """
    Gets the tcp listener and ask the database as soon as possible
    :return: nothing
    """
    tcpsock = on_init()
    tcpsock.connect(server)
    (sock, (ip, p)) = tcpsock.accept()
    # Gets the data
    sock.sendall(request)
    print("Query sent to", ip, ":", request)
    # get the result
    response = sock.recv()
    # Close the connection
    sock.close()
    tcpsock.close()
    return response

