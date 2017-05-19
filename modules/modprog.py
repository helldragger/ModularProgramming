"""ModularProgramming main script"""
import modules.kbinput as kbi


def on_init():
    kbi.set_hook()
    return


def on_exit():
    kbi.destroy_hook()
    return


def do_something():

    return


def init():
    on_init()
    run = True
    while run:
        # TODO add significant functionality
        do_something()
    on_exit()
    return
