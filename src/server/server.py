"""
The server initializer and main loop
"""

import src.server.net.communicator as comm


def run():
    """
    Launch the main loop
    :return: nothing
    """
    on_init()
    comm.run()
    return


def on_init():
    """
    Initialize the main vars, the database and vars
    :return: nothing
    """
    return

