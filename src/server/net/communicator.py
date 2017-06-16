"""Network-connection-to-network-queries layer"""

import socketserver

import src.server.manager.queries as manager


def send_message(message, sock):
    # recupération de la taille du message à envoyer et encodage
    size = str(len(message))
    # envoi de la taille du message, separateur, message
    sock.send((size+'\0'+message).encode())


def get_message(sock):
    # recupération de la taille du message et decodage
    header = sock.recv(1024).decode()
    head = header.split('\0')
    if len(head) != 2:
        return "ERROR: Client sent a wrong data format"
    # Recuperation de la taille du message sous forme numerique
    try:
        size = int(head[0])
    except Exception as e:
        return "ERROR: Invalid request size"
    # verification que la requete ne soit pas trop grande (on veut pas un overflow)
    if size > 1024:
        return "ERROR: Request too large"
    # instanciation des variables de recuperation des données
    data = [head[1]]
    data_received = len(head[1])
    while data_received < size:
        # recuperation d'un chunk
        chunk = sock.recv(1024).decode()
        # verification qu'on a pas recu un chunk vide (fin de transmission innattendue)
        if len(chunk) == 0:
            break
        # Add received chunk size to the total data received
        data_received += len(chunk)
        # add decoded received data to the total data
        data.append(chunk)
    # returns the whole data received
    result = "".join(data)
    return result


class QueryHandler(socketserver.BaseRequestHandler):
    """
    Request handler
    """

    def handle(self):
        print("Connected to", self.client_address)
        # get the query
        data = get_message(self.request)
        print("Query :", data)
        # analyze the query if sane
        if not data.startswith("ERROR:"):
            data = manager.analyze_query(data)
        else:
            print("Error occured: " + data)
        send_message(data, self.request)
        print("Response sent:", data)
        # close socket properly


def run():
    """
    Gets the tcp listener and launch new thread for each new connection.
    :return: nothing
    """
    host = 'localhost'
    port = 22220
    with socketserver.TCPServer((host, port), QueryHandler) as server:
        print("Server started on", host, ':', port)
        server.serve_forever()
