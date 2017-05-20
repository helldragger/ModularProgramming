"""Network-connection-to-network-queries layer"""

import socket as socket
import threading as thrd

import src.server.manager.queries as manager


port = 22222
ended = False


class Request(thrd.Thread):
    """
    Client-Server connection thread
    """
    def __init__(self, ip, p, sock):
        thrd.Thread.__init__(self)
        self.ip = ip
        self.port = p
        self.client = sock

    def run(self):
        print("New request from", self.ip, ":", self.port, '...')
        # Gets the data
        query = self.client.recv()
        print("Query received from", self.ip, ":", query)
        # Analyse the data
        response = manager.analyze_query(query)
        # Sends the result
        self.client.send(response)
        print("Response sent to", self.ip, ":", response)
        # Close the connection
        if response == "SERVER WILL BE TERMINATED":
            close()
        return


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
    tcpsock = on_init()
    thread_list = []
    while not ended:
        tcpsock.listen(10)
        (sock, (ip, p)) = tcpsock.accept()
        newthread = Request(ip, p, sock)
        thread_list.append(newthread)
        newthread.start()
    on_exit(thread_list)


def close():
    """
    Set the server to close
    :return: nothing
    """
    global ended
    ended = True
    return
