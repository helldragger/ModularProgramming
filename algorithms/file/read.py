def file_read(file_path, size=None):
    """
    Reads all the data from a file and returns it

    :param file_path: the location of the file
    :param size: the optional size of data to read from the file
    :return: the data
    """
    with open(file_path, 'r') as input_file:
        data = input_file.read(size)
    return data
