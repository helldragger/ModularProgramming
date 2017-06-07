"""
Communicate from the client to the server
"""

import socket


# First we get a connecting socket to etablish connection.
# When the connection is accepted, we send the query
# When the query is sent, we wait the server response
# We get the response then we close the connection


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
            sock.sendall(request.encode())
            print("Query sent")
            # Gets response
            print("Receiving response")
            response = sock.recv(4096).strip().decode()
            print("Response received:", response)
            # Close socket properly
            print("Closing connection...")
            sock.close()
            print("Connection closed")
        # returns response
        return response
    except Exception as e:
        with open("error_log.txt", 'w') as log:
            log.write(e)
        input("Enter anything to continue")
