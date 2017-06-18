import socketserver


class QueryHandler(socketserver.BaseRequestHandler):
    """
    Query handler
    """

    def handle(self):
        """
        Handle clients queries

        :return: nothing
        """
        return


def run_server():
    """
    Gets the tcp listener and launch new thread for each new connection.
    :return: nothing
    """
    # # CONSTANTS
    host = 'localhost'
    port = 25565
    # # FUNCTION
    with socketserver.TCPServer((host, port), QueryHandler) as server:
        print("Server started on", host, ':', port)
        server.serve_forever()
