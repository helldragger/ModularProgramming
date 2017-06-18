"""File system to database layer"""

import os

import src.db.errors as err


DATABASE_ROOT = os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, os.pardir, "algorithms")
caching_mode = False


def get_extensions(lang):
    """
    Determine the possible extensions of the file based on the language
    :return: The possible extensions of the file
    """
    extensions = {
        "python":    ['py'],
        "c":         ['c'],
        "fortran77": ['f', 'for'],
        "fortran95": ['f95.f'],
        "fortran90": ['f90.f'],
        "fortran03": ['f03.f']

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
    :return: the db file path or an Exception
    """
    if os.path.isdir(os.path.join(DATABASE_ROOT, algo_type)):
        extensions = get_extensions(algo_lang)
        for extension in extensions:
            file_path = os.path.join(algo_type, algo_spec + '.' + extension)
            print("Searching for", file_path)
            if os.path.isfile(os.path.join(DATABASE_ROOT, file_path)):
                return file_path
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
        lines = [line for line in file]
        if lines[0].startswith('needs '):
            temp = lines[0].lower().split()
            if len(temp) > 1:
                reqs = temp[1:]
            del lines[0]
        source = "".join(lines)
    return [reqs, source]


class Algorithm:
    """
    An algorithm file wrapper
    """
    def __init__(self, path):
        self.path = os.path.join(DATABASE_ROOT, path)
        if not os.path.isfile(self.path):
            raise err.DependenceNotFoundException(path)
        data = parse_file_data(self.path)
        self.requirements = data[0]
        self.source_code = data[1]
        print(path, " parsed.\nRequirements: \n\t", self.requirements, "\n")
