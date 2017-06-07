"""File system to database layer"""

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
        raise err.UnsupportedLanguageException(lang)
    else:
        return extensions[lang]


def get_file_path(algo_type, algo_spec, algo_lang):
    """
    Gets the file path if the algorithm is present in the database
    :param algo_type: the type of algorithm (the directory)
    :param algo_spec: the specific algorithm (the filename)
    :param algo_lang: the language of the specific algorithm (extension)
    :return: the file path or an Exception
    """
    if os.path.isdir(os.path.join(DATABASE_ROOT, algo_type)):
        extensions = get_extensions(algo_lang)
        for extension in extensions:
            filepath = os.path.join(DATABASE_ROOT, algo_type, algo_spec + '.' + extension)
            print("Searching for", filepath)
            if os.path.isfile(filepath):
                return filepath
        raise err.LanguageNotFoundException(algo_lang)
    else:
        raise err.TypeNotFoundException(algo_type)


def get_algorithm(path):
    """
    Returns the algorithm object from a specified path
    :return: the algorithm object
    """
    return Algorithm(path)


def parse_file_data(path):
    """
    Returns the requirements and source code of an algorithm file
    :param path: the algorithm file path
    :return: a tuple containing the requirements and the source code of the file
    """
    reqs = []
    source = ""
    with open(path, 'r') as file:
        lines = file.readlines()
        if lines[0].upper().startswith('NEEDS '):
            temp = lines[0].upper().split()
            if len(temp) > 1:
                reqs = temp[1:]
            del lines[0]
        source = "".join(lines)
    return reqs, source


class Algorithm:
    def __init__(self, path):
        self.path = path
        self.requirements, self.source_code = parse_file_data(path)
