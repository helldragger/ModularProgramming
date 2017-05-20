"""
The client hook
"""


import keyboard as kb


def on_init():
    """
    Registers hotkeys
    :return: nothing
    """
    kb.add_hotkey("ctrl+space", send_selec_and_get_answer)
    return


def send_selec_and_get_answer():
    """
    Send the selection to the server and write down the answer
    :return: nothing
    """
    # TODO the whole funciton and cocmmunicator
    return