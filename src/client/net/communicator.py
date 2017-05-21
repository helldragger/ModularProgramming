"""
Communicate from the client to the server
"""

import socket as socket


client = 'localhost'
server = 'localhost'
port_c_c_s = 22220
port_c_s_c = 22221
port_s_c_s = 22222
port_s_s_c = 22223


def on_init():
    """
    Initialize the tcp server and returns the input and output socket
    :return: the two sockets
    """
    # Opens a socket
    sock_c_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_c_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Binds the socket
    sock_c_s.bind((client, port_c_c_s))
    print('Client to server socket bind to', client, ':', port_c_c_s)
    # Opens a socket
    sock_s_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_s_c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Binds the socket
    sock_s_c.bind((client, port_c_s_c))
    print('Server to client socket bind to', client, ':', port_c_s_c)
    return sock_c_s, sock_s_c


def format_request(data):
    return bytes(source=data, encoding='utf8')


def deformat_response(data):
    return data.decode("utf-8")


def ask_database(request):
    """
    Gets the tcp listener and ask the database as soon as possible
    :return: nothing
    """
    request = format_request(request)
    print("Client initializing")
    sock_c_s, sock_s_c = on_init()
    print("Connection to the server")
    connected = False
    while not connected:
        print("Trying to connect to", server, ':', port_s_c_s)
        try:
            sock_c_s.connect((server, port_s_c_s))
            connected = True
        except Exception as e:
            pass
    print("Connected to the server")
    print("Sending query", request, "to the server")
    # Sends the query
    sock_c_s.send(request)
    print("Query sent to", server, ":", request)
    print("Listening for any answer on port", port_c_s_c)
    sock_s_c.listen(10)
    (sock_s, (ip, port_s)) = sock_s_c.accept()
    print("Receive response")
    # get the response
    response = sock_s.recv(1024)
    # Close the connection
    print("Closing the connection...")
    sock_c_s.close()
    sock_s_c.close()
    response = deformat_response(response)
    return response

