"""
The error messages of the server
"""


def invalid_arguments():
    """
    Returns the invalid argument error
    :return: the invalid argument error string
    """
    return "ERROR: INVALID ARGUMENTS, USE '<TYPE> <SPECIFIC> <LANGUAGE>'\
     or 'SERVER <COMMAND>'"


def unknown_server_command():
    """
    Returns the unknown server command error
    :return: the unknown server command error string
    """
    return "ERROR: UNKNOWN SERVER COMMAND."
