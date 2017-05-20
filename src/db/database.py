"""
The database hardware-to-memory layer
"""
import os

import src.db.errors as err


# Database format: { TypeOfAlgorithm1, TypeOfAlgorithm2...}
# -> TypeOfAlgorithm format: { SpecificAlgorithm1, SpecificAlgorithm2...}
# -> SpecificAlgorithm format: { Lang1, Lang2, Lang3....}
# -> Lang format : "Path\\To\\Correspondent\\Specific\\File"
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
    :return: nothing
    """

    # verify if all the cached files still exists
    dirs_to_verify = database.keys()
    for d in dirs_to_verify:
        specifics_to_verify = database[d].keys()
        for s in specifics_to_verify:
            lang_to_verify = database[d][s].keys()
            for l in lang_to_verify:
                if not os.path.isfile(database[d][s][l]):
                    del database[d][s][l]
            if len(database[d][s]) == 0:
                del database[d][s]
        if len(database[d]) == 0:
            del database[d]

    # adds new files to the database
    here = os.path.dirname(os.path.realpath(__file__))
    dbpath = os.path.join(here, os.pardir, "algorithms")
    for (type_dir, _, specific_files) in os.walk(dbpath):
        type_string = type_dir
        type_string.upper()
        # Create the specific dictionary if needed
        if database.get(type_string) is None:
            database[type_string] = {}

        for file_name in specific_files:
            specific_string = "".join(file_name.split('.')[:-1:])
            specific_string.upper()
            # Create the language dictionary if needed
            if database[type_string].get(specific_string) is None:
                database[type_string][specific_string] = {}

            # Determine the extension of the file
            file_extension = file_name.split('.')[-1]
            # Determine the language of the file
            language = detect_language(file_extension)
            # Adds it to the database if not there already
            if database[type_string][specific_string].get(language) is None:
                database[type_string][specific_string][language] = "\\".join([type_dir, file_name])
    return


def get_algorithm_string(path):
    """
    Returns the content of the algorithm contained in the file given in parameter
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
    if database.get(algo_type) is None:
        return err.type_not_found()
    if database[algo_type].get(algo_spec) is None:
        return err.specific_not_found()
    if database[algo_type][algo_spec].get(algo_lang) is None:
        return err.language_not_found(algo_lang)
    return get_algorithm_string(database[algo_type][algo_spec][algo_lang])
