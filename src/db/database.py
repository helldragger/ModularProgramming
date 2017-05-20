"""
The database hardware-to-memory layer
"""
import os
import threading
import time as t

import src.db.errors as err


database = None
updater = None


# Stoppable auto-updater to keep the database up to date
# and avoiding potential queries errors.
# Might be more efficient with a lot of queries than an update for each queries
# Might be less efficient in a light use but it should be fast enough
# to only leave a negligible footprint on such systems.
class Updater:
    """
    Auto updater class, can be paused.
    """
    def __init__(self):
        self._timer = None
        self.interval = 0.5
        self.is_running = False

    def _run(self):
        self.is_running = False
        self.start()
        update_database()

    def start(self):
        """
        Starts the timer if possible
        :return: nothing
        """
        if not self.is_running:
            self._timer = threading.Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        """
        Stops the timer if any
        :return: nothing
        """
        self._timer.cancel()
        self.is_running = False


def start_database():
    """
    Starts the auto updater
    :return: nothing
    """
    global database
    # TODO load the last memorized database
    # Database format: { TypeOfAlgorithm1, TypeOfAlgorithm2...}
    # -> TypeOfAlgorithm format: { SpecificAlgorithm1, SpecificAlgorithm2...}
    # -> SpecificAlgorithm format: { Lang1, Lang2, Lang3....}
    # -> Lang format : "Path\\To\\Correspondent\\Specific\\File"
    database = {}

    # Update the database once
    update_database()

    global updater
    # Start the auto updater
    updater = Updater()
    updater.start()
    return


def stop_database():
    """
    Stops the auto updater and destroy the remaining data of the database from memory
    :return: nothing
    """
    global updater
    updater.stop()
    while updater.is_running:
        t.sleep(1)
    # TODO serialize the memorized database
    global database
    del database
    return


def detect_language(filename):
    """
    Determine the language of the algorithm based on the file extension
    :return: The Langage used in the file
    """
    languages = {
        "PY": 'PYTHON',
        "C":  'C'
    }
    extension = filename.split('.')[-1].upper()
    if extension not in languages:
        return "UNDETERMINED"
    else:
        return languages[extension]


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
    global updater
    global database
    updater.stop()
    while updater.is_running:
        t.sleep(0.1)
    updater.can_update = False
    if database.get(algo_type) is None:
        return err.type_not_found()
    if database[algo_type].get(algo_spec) is None:
        return err.specific_not_found()
    if database[algo_type][algo_spec].get(algo_lang) is None:
        return err.language_not_found(algo_lang)
    data = get_algorithm_string(database[algo_type][algo_spec][algo_lang])
    updater.start()
    return data


def update_database():
    """
    Update the database with the current database state.
    :return: nothing
    """
    global database
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
    dbpath = os.path.join(here, os.pardir, os.pardir, "algorithms")
    for (type_dir, _, specific_files) in os.walk(dbpath):
        if len(specific_files) == 0:
            continue
        type_dir = type_dir.split('\\')[-1]
        type_s = type_dir.upper()
        # Create the specific dictionary if needed
        if database.get(type_s) is None:
            database[type_s] = {}

        for file_name in specific_files:
            specific_s = "".join(file_name.split('.')[:-1:]).upper()
            # Create the language dictionary if needed
            if database[type_s].get(specific_s) is None:
                database[type_s][specific_s] = {}

            # Determine the extension of the file
            file_extension = file_name.split('.')[-1].upper()
            # Determine the language of the file
            l = detect_language(file_extension)
            # Adds it to the database if not there already
            if database[type_s][specific_s].get(l) is None:
                database[type_s][specific_s][l] = "\\".join([type_dir, file_name])
    return
