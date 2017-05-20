"""ModularProgramming server side"""

import socket as sock

import src.server.manager.queries as que


# Opens a socket
def listen_to_interweb():
    """
    Listen to the interweb for incoming connections
    :return:
    """
    listener = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
    listener.bind(('', 22222))

    while True:
        listener.listen(5)
        client, address = listener.accept()

        data = client.recv(255)
        if data != "":
            result = que.on_call(data)
            client.send(result)
        client.close()
        listener.close()
        return


# Binds the socket
# Gets the data
# Analyse the data
# Sends the result
# Close the connection
