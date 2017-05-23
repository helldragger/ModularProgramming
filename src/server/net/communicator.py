"""Network-connection-to-network-queries layer"""

import socketserver

import src.server.manager.queries as manager


class QueryHandler(socketserver.BaseRequestHandler):
    """
    Request handler
    """

    def handle(self):
        print("Connected to", self.client_address)
        # get the query
        data = self.request.recv(1024).strip().decode()
        print("Query :", data)
        # analyze the query
        data = manager.analyze_query(data)
        # send the response
        self.request.sendall(data.encode())
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
