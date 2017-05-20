"""Network-queries-to-script-queries layer"""

import src.db.manager as db
import src.server.manager.errors as err
import src.server.net.communicator as net

def analyze_query(query_string):
    """
    Sanitize and format the query to ask the database and returns the result or error
    :param query_string: the query string send by TCP
    :return: the result or corresponding error
    """
    # Sanitize query string: only upper case
    query_string.upper()
    # Split query string into arguments
    query = query_string.split(' ')
    # Verify arguments count
    if len(query) == 2:
        # Verify if "server close" was issued
        if query[0] == "SERVER":
            if query[1] == "CLOSE":
                net.close()
                return "SERVER TERMINATED"
            else:
                return err.unknown_server_command()
    elif len(query) == 3:
        # Send the query to the database
        result = db.ask_database(tuple(query))
        # Send the result back to the TCP socket
        return result
    else:
        # Invalid arguments
        return err.invalid_arguments()
