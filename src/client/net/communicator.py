"""
Communicate from the client to the server
"""

import socket


# First we get a connecting socket to etablish connection.
# When the connection is accepted, we send the query
# When the query is sent, we wait the server response
# We get the response then we close the connection


def send_message(message, sock):
    size = str(len(message))
    sock.sendall((size+'\0'+message).encode())


def get_message(sock):
    header = sock.recv(1024).decode()
    head = header.split('\0')
    if len(head) != 2:
        return "ERROR: Server sent a wrong data format"
    try:
        size = int(head[0])
    except Exception as e:
        return "ERROR: Server sent a wrong data size"
    data = [head[1]]
    data_received = len(head[1])
    while data_received < size:
        chunk = sock.recv(1024).decode()
        if len(chunk) == 0:
            return "ERROR: DATA TRANSMISSION INTERRUPTED BY THE SERVER"
        data_received += len(chunk)
        data.append(chunk.strip())
    return "".join(data)


def ask_database(request):
    """
    Gets the tcp listener and ask the database as soon as possible

    :return: the database response
    """
    server = 'localhost'
    port = 22220
    # creates the socket
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # connect to the server
            print("Connecting to the server")
            sock.connect((server, port))
            print("Connected")
            # Sends query
            print("Sending the query:", request)
            send_message(request, sock)
            print("Query sent")
            # Gets response
            print("Receiving response")
            response = get_message(sock)
            print("Response received:", response)
            # Close socket properly
            print("Closing connection...")
            sock.close()
            print("Connection closed")
        # returns response
        return response
    except Exception as e:
        with open("error_log.txt", 'w') as log:
            log.write(str(e))
        input("Enter anything to continue")
