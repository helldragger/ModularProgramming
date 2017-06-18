import socket


def connect_to_server():
    """
    Connects to the server once over TCP

    :return: nothing
    """
    # # CONSTANTS
    server = 'localhost'
    port = 25565
    # # FUNCTION
    # creates the socket
    try:
        # attempts to make a TCP connection with the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # connect to the server
            sock.connect((server, port))
            # properly closes the socket
            sock.shutdown()
            sock.close()
        return
    except Exception as e:
        with open("error_log.txt", 'w') as log:
            log.write(str(e).encode())
