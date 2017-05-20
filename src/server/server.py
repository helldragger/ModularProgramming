"""
The server initializer and main loop
"""


def run():
    try:
        on_init()
    except Exception as e:
        print(e)
    finally:
        on_close()
    return


def on_init():
    """
    Initialize the main vars, the database and vars
    :return: nothing
    """
    return


def on_close():
    """
    Close the necessary things like remaining sockets, database, and streams
    :return: nothing
    """
    return
