"""Network-connection-to-network-queries layer"""

import socket as socket
import threading as thrd

import src.server.manager.queries as manager


server = 'localhost'
port_c_c_s = 22220
port_c_s_c = 22221
port_s_c_s = 22222
port_s_s_c = 22223
ended = False


def format_response(data):
    return bytes(source=data, encoding='utf8')


def deformat_query(data):
    return str(data.decode("utf-8"))


class Request(thrd.Thread):
    """
    Client-Server connection thread
    """
    def __init__(self, ip, sock_c_s):
        thrd.Thread.__init__(self)
        self.ip = ip
        self.socket_c_s = sock_c_s
        # Opens a socket
        sock_s_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_s_c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Binds the socket
        sock_s_c.bind((server, port_s_s_c))
        self.socket_s_c = sock_s_c

    def run(self):
        print("New request from", self.ip, ":", port_c_c_s, '...')
        # Gets the data
        query = self.socket_c_s.recv(1024)
        print("Query received from client =", query)
        # Analyse the data
        query = deformat_query(query)
        response = manager.analyze_query(query)
        print("Connection to the client to send response")
        connected = False
        while not connected:
            print("Trying ot connect to", self.ip, ':', port_c_s_c)
            try:
                self.socket_s_c.connect((self.ip, port_c_s_c))
                connected = True
            except Exception as e:
                pass
        print("Connected to client")
        # Sends the result
        response = format_response(str(response))
        self.socket_s_c.send(response)
        print("Response sent to client =", response)
        # Close the connection
        self.socket_c_s.close()
        self.socket_s_c.close()
        if response == "SERVER WILL BE TERMINATED":
            close()
        return


def on_init():
    """
    Initialize the tcp server and returns the input and output socket
    :return: the two sockets
    """
    # Opens a socket
    sock_c_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_c_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Binds the socket
    sock_c_s.bind((server, port_s_c_s))
    return sock_c_s


def on_exit(threads):
    """
    Terminate unterminated threads
    :param threads: the cached threads
    :return: nothing
    """
    for t in threads:
        del t


def run():
    """
    Gets the tcp listener and launch new thread for each new connection.
    :return: nothing
    """
    print("Server initialization...")
    sock_c_s = on_init()
    thread_list = []
    print("Server started... Waiting for incoming connections...")
    while not ended:
        print("Listening on port", port_s_c_s)
        sock_c_s.listen(10)
        (sock_c, (ip, port_c)) = sock_c_s.accept()
        newthread = Request(ip, sock_c)
        thread_list.append(newthread)
        newthread.start()
    print("Server exiting...")
    sock_c_s.close()
    sock_s_c.close()
    on_exit(thread_list)


def close():
    """
    Set the server to close
    :return: nothing
    """
    global ended
    ended = True
    return
