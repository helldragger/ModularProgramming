"""
The database hardware-to-memory layer
"""
import os


database = {}


def detect_language(filename):
    """
    Determine the language of the algorithm based on the file extension
    :return: The Langage used in the file
    """
    languages = {
        "py": 'PYTHON',
        "c":  'C'
    }
    extension = filename.split('.')[-1]
    if extension not in languages:
        return "UNDETERMINED"
    else:
        return languages[extension]


def update_database():
    """
    Update the database with the current database state.
    :return:
    """

    # verify if all the cached files still exists
    keys_to_verify = database.keys()
    for key in keys_to_verify:
        path, _ = database[key]
        if not os.path.isfile(path):
            del database[key]

    # adds new files to the database
    here = os.path.dirname(os.path.realpath(__file__))
    dbpath = os.path.join(here, os.pardir, "algorithms")
    for (dir_path, _, files_names) in os.walk(dbpath):
        for file_name in files_names:
            alias = " \\".join([dir_path, file_name])
            if alias not in keys_to_verify:
                # Saves the file path to the database plus determined language
                database[alias] = ("\\".join([dir_path, file_name]), detect_language(file_name))
    return


def get_algorithm(key):
    """
    Returns the content of the algorithm
    :return: a string of the algorithm
    """
    path = database[key][0]
    with open(path, 'r') as file:
        string = "".join(file.readlines())
        return string


def does_key_exists(key):
    """
    Returns if there actually is an registered entry to this key
    :param key: the key to test
    :return: if there is a result or not
    """
    return key in database.keys()
