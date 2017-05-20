"""
The database hardware-to-memory layer
"""
import os

import src.db.errors as err


DATABASE_ROOT = os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, "algorithms")


def get_extension(lang):
    """
    Determine the extension of the file based on the language
    :return: The extension of the file
    """
    extensions = {
        "PYTHON": 'PY',
        "C":  'C'
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
        extension = get_extension(algo_lang)
        if os.path.isfile(os.path.join(DATABASE_ROOT, algo_type, algo_spec + '.' + extension)):
            return get_algorithm_string(os.path.join(DATABASE_ROOT, algo_type, algo_spec + '.' + extension))
        else:
            return err.language_not_found(algo_lang)
    else:
        return err.type_not_found()
