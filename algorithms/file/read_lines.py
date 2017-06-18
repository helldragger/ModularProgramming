def file_read_lines(file_path):
    """
    Reads all the lines from a file and returns them

    :param file_path: the location of the file
    :return: the data
    """
    with open(file_path, 'r') as input_file:
        lines = [line for line in input_file]
    return lines
