def network_receive_once(sock):
    """
    Receive a message from a connected socket in the following format 'size\0message' if any.
    Not fit to be used to receive multiple messages at once.

    :param sock: the connected socket
    :return: the message if any
    """
    # # CONSTANTS
    buffer_size = 1024
    # Set max_data_size to 0 if you want unlimited data size to receive
    max_data_size = 1024

    # # FUNCTION
    # gets the header if any
    header = sock.recv(buffer_size).decode()

    # if none, return nothing
    if len(header) == 0:
        return ''
    # else, split the size from the start of the data
    head = header.split('\0')
    if len(head) != 2:
        raise Exception("ERROR: Received a wrong header format")

    # Retrieving the data size
    try:
        size = int(head[0])
    except ValueError:
        raise Exception("ERROR: Invalid request size")

    # verification que la requete ne soit pas trop grande (on veut pas un overflow)
    if max_data_size != 0 and size > max_data_size:
        raise Exception("ERROR: Data to receive is too large")

    data = [head[1]]
    data_received = len(head[1])
    error_counter = 0
    while data_received < size:
        # we get a chunk of data to receive
        chunk = sock.recv(buffer_size).decode()
        # if there is missing data, we throw an exception after three tries
        if len(chunk) == 0:
            if error_counter == 3:
                raise Exception("ERROR: Data missing")
            else:
                error_counter += 1
        else:
            # we dd received chunk size to the total data received
            data_received += len(chunk)
            # we add decoded received data to the total data
            data.append(chunk)

    # returns the whole data received
    result = "".join(data)
    return result
