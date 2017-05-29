"""
The database hardware-to-memory layer
"""
import os

import src.db.errors as err


DATABASE_ROOT = os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, os.pardir, "algorithms")


def get_extensions(lang):
    """
    Determine the possible extensions of the file based on the language
    :return: The possible extensions of the file
    """
    extensions = {
        "PYTHON":    ['PY'],
        "C":         ['C'],
        "FORTRAN77": ['F', 'FOR'],
        "FORTRAN95": ['F95.F'],
        "FORTRAN90": ['F90.F'],
        "FORTRAN03": ['F03.F']

    }

    if lang not in extensions.keys():
        return "UNDETERMINED"
    else:
        return extensions[lang]


def get_algorithm_string(path):
    """
    Returns the content of the algorithm contained in the specified file
    :param path: the file path
    :return: a string of the algorithm
    """
    with open(path, 'r') as file:
        string = "".join(file.readlines())
        return string


def get_algorithm(algo_type, algo_spec, algo_lang):
    """
    Evaluate the query asked
    :param algo_type: the type of algorithm (the directory)
    :param algo_spec: the specific algorithm (the filename)
    :param algo_lang: the language of the specific algorithm (extension)
    :return: the result
    """

    if os.path.isdir(os.path.join(DATABASE_ROOT, algo_type)):
        extensions = get_extensions(algo_lang)
        if extensions == "UNDETERMINED":
            return err.language_not_supported()
        for extension in extensions:
            filepath = os.path.join(DATABASE_ROOT, algo_type, algo_spec + '.' + extension)
            print("Searching for", filepath)
            if os.path.isfile(filepath):
                return get_algorithm_string(filepath)
        return err.language_not_found(algo_lang)
    else:
        return err.type_not_found()
