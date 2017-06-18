def file_write(file_path, data):
    """
    Write data in the file specified at file_path

    :param file_path: the location of the file
    :param data: the data to write
    :return: nothing
    """
    with open(file_path, 'w') as output_file:
        if not isinstance(data, str):
            data = str(data)
        output_file.write(data.encode())
    return
