def network_send_once(message, sock):
    """
    Sends the size of the message and itself in the following format: 'size\0message'.
    Not fit to be used to send multiple messages at once.

    :param message: the message to send
    :param sock: the connected socket to use
    :return: nothing
    """
    # Gets the total size of the message to send as a string
    size = str(len(message))
    # sends the total size and the message separated by a null character
    sock.sendall((size+'\0'+message).encode())
    return
