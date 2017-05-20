"""
The server initializer and main loop
"""

import src.db.manager as db
import src.server.net.communicator as comm


def run():
    """
    Launch the main loop
    :return: nothing
    """
    on_init()
    comm.run()
    on_close()
    return


def on_init():
    """
    Initialize the main vars, the database and vars
    :return: nothing
    """
    db.start_database()
    return


def on_close():
    """
    Terminate the database and main processes
    :return: nothing
    """
    db.stop_database()
    return
