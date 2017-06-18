"""
Communicate from the keyboard hook to the python server
"""
import sys

import communicator as net


def write_response(response):
    """
    Write the server answer into a temporary file shared with the AHK script
    :param response: the server answer
    :return: nothing
    """
    with open("temp.txt", 'w') as temp:
        temp.write(response)
    return


def is_valid_request():
    """
    Determines if there is enough args passed to be a valid request
    :return: if there is or not
    """
    if len(sys.argv) != 4:
        write_response("ERROR: INVALID ARGUMENTS, USE '<TYPE> <SPECIFIC>\
                        <LANGUAGE>' or 'SERVER <COMMAND>'")
        return False
    return True


def run():
    """
    Run the script
    :return: nothing
    """
    if is_valid_request():
        request = " ".join(sys.argv[1:])
        response = net.ask_database(request)
        write_response(response)
    return

run()
