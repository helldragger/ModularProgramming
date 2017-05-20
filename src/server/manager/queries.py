"""Network queries"""
import src.algoutput as algo
import src.errors as err


def on_call(s):
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

