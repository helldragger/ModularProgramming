"""
Communicate from the keyboard hook to the python server
"""
import sys

import src.client.net.communicator as net


def write_response(response):
    with open("temp.txt", 'w') as temp:
        temp.write(response)
    return


def run(request):
    response = net.ask_database(request)
    write_response(response)
    return

run(sys.argv[1])
