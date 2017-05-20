"""
The server initializer and main loop
"""

import src.server.net.communicator as comm


def run():
    """
    Launch the main loop
    :return: nothing
    """
    comm.run()
    return

