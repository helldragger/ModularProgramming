"""Keyboard hook to watch for hotkey calls"""
import modules.algoutput as algo
import modules.errors as err


def set_hook():
    # TODO make sure we have access to keyboard input and output
    return


def destroy_hook():
    # TODO revoke cleanly our access to the keyboard
    return


def set_hotkey():
    # TODO when hotkey triggered: calls on_call()
    return


def destroy_hotkey():
    # TODO Clear the hotkey
    return


def on_call():
    s = get_input()
    try:
        eval_selection(s)
        algo.get_algo_string(s)
    except Exception as e:
        err.input_unrecognized(e)
    finally:
        return


def get_input():
    return format_selection( get_selection( ) )


def format_selection():
    # TODO sanitize user's selection
    return


def get_selection():
    # TODO get the selected text and try to format it in a usable way
    return


def eval_selection():
    # TODO verify if user input is meaningful for the program
    return

